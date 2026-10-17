"""nano/verdict.py: the statistics every verified or stackable result rests on. CPU only, standard library."""
import math
import random
import statistics

from nano import verdict as V


def test_welch_and_t_tail():
    t, df = V.welch([1.0, 2.0, 3.0], [2.0, 3.0, 4.0])
    assert abs(t - 1.0 / math.sqrt(2.0 / 3.0)) < 1e-9 and abs(df - 4.0) < 1e-9
    assert V.welch([1.0], [2.0, 3.0]) == (None, None)
    assert abs(V.t_sf(0.0, 7) - 0.5) < 1e-12
    assert abs(V.t_sf(2.776445, 4) - 0.025) < 1e-4            # table value of t(0.975, 4)
    assert abs(V.t_sf(-2.776445, 4) - 0.975) < 1e-4


def _e_numeric(diffs, sigma, margin, tau):
    """The half-normal mixture of Gaussian likelihood ratios, integrated by the midpoint rule."""
    def lr(delta):
        return math.exp(sum(((d - margin) * delta - delta * delta / 2) for d in diffs) / sigma ** 2)
    h, total = tau / 2000, 0.0
    for i in range(20000):
        x = (i + 0.5) * h
        total += 2 / (tau * math.sqrt(2 * math.pi)) * math.exp(-x * x / (2 * tau * tau)) * lr(x) * h
    return total


def test_e_value_closed_form_matches_the_mixture_integral():
    for diffs, sigma, margin, tau in (([0.01, 0.004, 0.008], 0.006, 0.002, 0.009), ([-0.003, 0.001], 0.005, 0.0, 0.005),
                                      ([0.02, 0.018, 0.025, 0.02], 0.01, 0.005, 0.015)):
        closed = V.e_value(diffs, sigma, margin, tau=tau)
        assert abs(closed - _e_numeric(diffs, sigma, margin, tau)) / closed < 1e-3, diffs
    assert V.e_value([], 0.01) == 1.0
    d = [0.01, 0.012, 0.009]
    assert V.e_value(d, 0.005, 0.0) > V.e_value(d, 0.005, 0.005) > V.e_value(d, 0.005, 0.01)   # one-sided in the margin


def test_e_value_has_mean_at_most_one_under_the_null():
    rng = random.Random(0)
    sims = [V.e_value([rng.gauss(0.0, 1.0) for _ in range(4)], 1.0, 0.0, tau=1.5) for _ in range(20000)]
    assert statistics.mean(sims) < 1.05


def test_e_bh():
    assert V.e_bh({}, 0.1) == set()
    # m = 4, alpha 0.1: thresholds m/(k alpha) = 40, 20, 13.3, 10
    assert V.e_bh({"a": 45, "b": 25, "c": 2, "d": 1}, 0.1) == {"a", "b"}
    assert V.e_bh({"a": 39, "b": 25, "c": 2, "d": 1}, 0.1) == {"a", "b"}    # the step-up passes k = 2 even if e_(1) < 40
    assert V.e_bh({"a": 19, "b": 15, "c": 2, "d": 1}, 0.1) == set()
    # adding candidates with small e-values to the family raises every threshold
    assert V.e_bh({"a": 120}, 0.01) == {"a"} and V.e_bh({"a": 120, "b": 1, "c": 0.5}, 0.01) == set()


def test_sigma_rule_uses_the_baseline_only_and_a_true_upper_bound():
    assert V.sigma_upper(1.0, 4, 0.10) > V.sigma_upper(1.0, 4, 0.25) > 1.0
    assert abs(V.sigma_upper(1.0, 30, 0.50) - 1.0) < 0.02                    # q 0.5 is about the median, not a bound
    assert V.sigma_quantile(4) == 0.10 and V.sigma_quantile(5) == 0.25
    base = [3.30, 3.31, 3.295, 3.305, 3.302, 3.308]
    sd, up, df = V.baseline_sigma(base)
    assert df == 5 and abs(sd - statistics.stdev(base)) < 1e-12 and abs(up - V.sigma_upper(sd, 5, 0.25)) < 1e-12
    a = V.sequential_verdict([3.29, 3.29, 3.29], base, lower_is_better=True)
    b = V.sequential_verdict([3.20, 3.31, 3.25], base, lower_is_better=True)
    assert a["sd_diff_used"] == b["sd_diff_used"] == round(math.sqrt(2) * up, 5)   # candidate runs never move sigma
    assert V.sequential_verdict([3.2], [3.3], lower_is_better=True)["status"] == "error"


def test_pairing_is_by_seed_number():
    base, bseeds = [1.0, 2.0, 3.0], [0, 1, 2]
    assert V.paired_diffs([0.5, 2.5], base, [0, 2], bseeds) == [0.5, 0.5]         # seed 1 errored: seed 2 meets seed 2
    assert V.paired_diffs([0.5], base, [7], bseeds) == [1.5]                      # no baseline seed 7: the mean
    assert V.paired_diffs([0.5, 2.5], base) == [0.5, -0.5]                        # no ids: by position
    v = V.sequential_verdict([0.9, 1.9, 2.9], [1.0, 3.0, 2.0], cand_seeds=[0, 1, 2], base_seeds=[0, 2, 1], lower_is_better=True)
    assert abs(v["gain"] - 0.1) < 1e-9


def test_futility_and_tiers():
    base = [3.30, 3.31, 3.295, 3.305, 3.302, 3.308]
    assert V.futility([3.4, 3.35], base, lower_is_better=True)
    assert not V.futility([3.4, 3.30], base, lower_is_better=True) and not V.futility([3.4], base, lower_is_better=True)
    assert V.sequential_verdict([3.40], base, lower_is_better=True)["status"] == "fail"
    assert V.sequential_verdict([3.29], base, lower_is_better=True)["status"] == "promising"
    assert V.sequential_verdict([3.25, 3.25, 3.25, 3.25], base, lower_is_better=True)["status"] == "verified"
    # higher-is-better scores are negated, so the same gap in the other direction is the same verdict
    assert V.sequential_verdict([-3.25] * 4, [-x for x in base], lower_is_better=False)["status"] == "verified"


def _false_verified_rate(n_base, sims=2000, max_seeds=5, margin=0.005, sd=0.004, seed=11):
    """Candidates exactly at the margin (the worst case of the null), stopped the moment they verify."""
    rng = random.Random(seed)
    hits = 0
    for _ in range(sims):
        base = [3.3 + rng.gauss(0, sd) for _ in range(n_base)]
        cand = []
        for _ in range(max_seeds):
            cand.append(3.3 - margin + rng.gauss(0, sd))
            if V.sequential_verdict(cand, base, margin=margin, alpha=0.01, lower_is_better=True)["status"] == "verified":
                hits += 1
                break
    return hits / sims


def test_optional_stopping_keeps_the_false_verified_rate_below_alpha():
    assert _false_verified_rate(6) < 0.01          # the default baseline (6 runs, 75% bound)
    assert _false_verified_rate(5, seed=12) < 0.01  # 5 runs, 90% bound


def test_loser_still_promising_is_not_a_problem():
    from nano import controls
    assert controls.judge_overnight("lr_x10", "promising")["ok"]
    assert not controls.judge_overnight("lr_x10", "stackable")["ok"]
