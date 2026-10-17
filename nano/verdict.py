"""Statistics for the ladder and the overnight verdict, with no dependency beyond the standard library.

Verdict rule (following the two public speedruns: modded-nanogpt asks for p < 0.01 on the mean,
parameter-golf for a 0.005-nat margin as well): a candidate is verified when its mean score
beats the pooled baseline mean by more than `margin` AND a one-sided Welch t-test gives
p < `alpha`, with at least `min_seeds` runs on each side.

Direction: the verdict functions take raw scores in the profile's units. When the active profile is
higher-is-better (PF.current().lower_is_better is False) the values are negated first, so `gain` is
always positive when the candidate is better; pass lower_is_better= to override the profile. Better than the mean but not significant
is a close call; better with too few seeds is promising; otherwise it failed.

Rung calibration: the baseline's loss curves from several seeds give, at every step, the spread
across seeds of the windowed mean loss. A candidate's matched-step gap is reported in units of
that spread (z), so thresholds are statistical rather than guessed.
"""
from __future__ import annotations

import math
import statistics


def _lower_is_better(flag: bool | None) -> bool:
    if flag is not None:
        return bool(flag)
    try:
        from nano.ideate import lower_is_better
        return lower_is_better()
    except Exception:  # noqa: BLE001
        return True


def oriented(vals: list[float], lower_is_better: bool | None = None) -> list[float]:
    """Raw scores turned lower-is-better (negated for a higher-is-better profile)."""
    return list(vals) if _lower_is_better(lower_is_better) else [-v for v in vals]


# ---------------------------------------------------------------- incomplete beta (Numerical Recipes betacf)
def _betacf(a: float, b: float, x: float, max_iter: int = 300, eps: float = 3e-14) -> float:
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / d if abs(d) > 1e-300 else 1e300
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / d if abs(d) > 1e-300 else 1e300
        c = 1.0 + aa / c if abs(c) > 1e-300 else 1e300
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / d if abs(d) > 1e-300 else 1e300
        c = 1.0 + aa / c if abs(c) > 1e-300 else 1e300
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def betainc(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1.0 - x)
    front = math.exp(lbeta)
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def t_sf(t: float, df: float) -> float:
    """One-sided survival function of Student's t: P(T > t)."""
    if df <= 0:
        return 0.5
    x = df / (df + t * t)
    tail = 0.5 * betainc(df / 2.0, 0.5, x)
    return tail if t >= 0 else 1.0 - tail


def welch(a: list[float], b: list[float]) -> tuple[float | None, float | None]:
    """Welch's t statistic and degrees of freedom for mean(b) - mean(a) > 0 (b worse than a means t < 0)."""
    if len(a) < 2 or len(b) < 2:
        return None, None
    ma, mb = statistics.mean(a), statistics.mean(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    se2 = va / len(a) + vb / len(b)
    if se2 <= 0:
        return (math.inf if mb > ma else (-math.inf if mb < ma else 0.0)), float(len(a) + len(b) - 2)
    t = (mb - ma) / math.sqrt(se2)
    df = se2 ** 2 / ((va / len(a)) ** 2 / (len(a) - 1) + (vb / len(b)) ** 2 / (len(b) - 1))
    return t, df


def verdict(cand_vals: list[float], base_vals: list[float], *, margin: float = 0.005, alpha: float = 0.01,
            min_seeds: int = 3, lower_is_better: bool | None = None) -> dict:
    """Candidate and baseline scores (raw; negated here when the profile is higher-is-better)."""
    cand_vals, base_vals = oriented(cand_vals, lower_is_better), oriented(base_vals, lower_is_better)
    out = {"n_cand": len(cand_vals), "n_base": len(base_vals), "margin": margin, "alpha": alpha}
    if not cand_vals or not base_vals:
        out.update({"status": "error", "gain": None, "p": None})
        return out
    gain = statistics.mean(base_vals) - statistics.mean(cand_vals)
    out["gain"] = round(gain, 5)
    t, df = welch(cand_vals, base_vals)           # t > 0 when the baseline mean is higher (candidate better)
    p = t_sf(t, df) if t is not None and df is not None and math.isfinite(t) else (0.0 if t == math.inf else None)
    out.update({"t": None if t is None or not math.isfinite(t) else round(t, 3), "df": None if df is None else round(df, 2),
                "p": None if p is None else round(p, 5)})
    if gain <= 0:
        out["status"] = "fail"
    elif len(cand_vals) < min_seeds or len(base_vals) < min_seeds:
        out["status"] = "promising"
    elif gain > margin and p is not None and p < alpha:
        out["status"] = "verified"
    else:
        out["status"] = "close_call"
    return out


# ---------------------------------------------------------------- curve calibration
def window_means(curve: list[float], window: int) -> list[float | None]:
    """Mean over the trailing window at every step (None until the window fills)."""
    out: list[float | None] = []
    for i in range(len(curve)):
        if i + 1 < window:
            out.append(None)
            continue
        seg = [v for v in curve[i + 1 - window: i + 1] if v == v]
        out.append(sum(seg) / len(seg) if seg else None)
    return out


def noise_curve(curves: list[list[float]], window: int) -> list[float | None]:
    """Spread across seeds of the windowed mean score at every step (sample SD; None where undefined)."""
    if len(curves) < 2:
        return [None] * (len(curves[0]) if curves else 0)
    wm = [window_means(c, window) for c in curves]
    n = min(len(w) for w in wm)
    out: list[float | None] = []
    for i in range(n):
        vals = [w[i] for w in wm if w[i] is not None]
        out.append(statistics.stdev(vals) if len(vals) >= 2 else None)
    return out


def z_of(gap: float | None, sd: float | None, floor: float = 1e-3) -> float | None:
    if gap is None or sd is None:
        return None
    return round(gap / max(sd, floor), 2)


# ---------------------------------------------------------------- anytime-valid sequential test (optional stopping is safe)
def _chi2_lower_quantile(df: int, q: float = 0.10) -> float:
    """Lower q-quantile of chi-square with df degrees of freedom (Wilson-Hilferty approximation)."""
    z = {0.05: -1.6449, 0.10: -1.2816, 0.20: -0.8416, 0.25: -0.6745, 0.40: -0.2533, 0.50: 0.0}.get(q, -1.2816)
    h = 2.0 / (9.0 * df)
    return df * (1.0 - h + z * math.sqrt(h)) ** 3


def sigma_upper(sd: float, df: int, q: float = 0.50) -> float:
    """A conservative (1-q) upper confidence bound on the true SD from a sample SD with df degrees of
    freedom: sd * sqrt(df / chi2_q(df)). With few seeds this is much larger than the point estimate,
    which is the price of treating sigma as known in the e-process."""
    if df <= 0:
        return sd * 3.0
    return sd * math.sqrt(df / max(_chi2_lower_quantile(df, q), 1e-9))


def e_value(diffs: list[float], sigma: float, margin: float = 0.0, tau: float | None = None) -> float:
    """One-sided Gaussian-mixture e-value for H0: mean(diff) <= margin, sigma treated as known.
    diffs are per-seed (baseline - candidate) differences, positive = candidate better. Half-normal
    prior on the effect with SD tau (default sigma). Closed form:
        a = n/sigma^2 + 1/tau^2,  b = S/sigma^2,  E = 2/(tau*sqrt(a)) * exp(b^2/(2a)) * Phi(b/sqrt(a)).
    E is a nonnegative supermartingale under H0, so P(sup E >= 1/alpha) <= alpha for any stopping rule."""
    n = len(diffs)
    if n == 0:
        return 1.0
    sigma = max(sigma, 1e-4)                      # a floor: five identical seeds do not mean zero noise
    tau = sigma if tau is None else tau
    S = sum(d - margin for d in diffs)
    a = n / (sigma * sigma) + 1.0 / (tau * tau)
    b = S / (sigma * sigma)
    phi = 0.5 * (1.0 + math.erf((b / math.sqrt(a)) / math.sqrt(2.0)))
    expo = min(b * b / (2.0 * a), 700.0)         # e-values beyond e^700 are "infinite" for every purpose here
    return 2.0 / (tau * math.sqrt(a)) * math.exp(expo) * phi


def e_bh(evalues: dict[str, float], alpha: float = 0.01) -> set[str]:
    """e-BH: reject the k largest e-values with e_(k) >= m / (k * alpha); FDR <= alpha under any dependence."""
    m = len(evalues)
    if m == 0:
        return set()
    order = sorted(evalues.items(), key=lambda kv: -kv[1])
    k_star = 0
    for k, (_, e) in enumerate(order, 1):
        if e >= m / (k * alpha):
            k_star = k
    return {cid for cid, _ in order[:k_star]}


def pooled_sd(cand_vals: list[float], base_vals: list[float]) -> tuple[float, int]:
    """Pooled within-group SD of single runs and its degrees of freedom."""
    ss, df = 0.0, 0
    for vals in (cand_vals, base_vals):
        if len(vals) >= 2:
            m = statistics.mean(vals)
            ss += sum((v - m) ** 2 for v in vals)
            df += len(vals) - 1
    return (math.sqrt(ss / df) if df > 0 else 0.0), df


def sequential_verdict(cand_vals: list[float], base_vals: list[float], *, margin: float = 0.005, alpha: float = 0.01,
                       stackable_margin: float = 0.002, stackable_alpha: float = 0.05, min_seeds: int = 3,
                       sign_consistent: bool | None = None, lower_is_better: bool | None = None) -> dict:
    """The verdict used overnight; valid under any seed-adding or stopping rule.
    Candidate seed i is paired with baseline seed i where both exist (shared data order), extra
    candidate seeds are compared with the baseline mean. The per-difference SD is sqrt(2) times a
    conservative upper bound on the pooled single-run SD. Tiers:
      verified  : E >= 1/alpha for `margin`, n >= min_seeds
      stackable : E >= 1/stackable_alpha for `stackable_margin`, n >= min_seeds, rung gaps of one sign;
                  feeds composition and promotion-by-accumulation, never a win on its own
      close_call: better than the baseline mean but neither tier
      promising : better with fewer than min_seeds
      fail      : not better
    The Welch p is reported for reference only. Scores are raw; see the module note on direction."""
    cand_vals, base_vals = oriented(cand_vals, lower_is_better), oriented(base_vals, lower_is_better)
    out = {"n_cand": len(cand_vals), "n_base": len(base_vals), "margin": margin, "alpha": alpha}
    if not cand_vals or len(base_vals) < 2:
        out.update({"status": "error", "gain": None, "e": None, "e_stack": None, "p": None})
        return out
    base_mean = statistics.mean(base_vals)
    sd, df = pooled_sd(cand_vals, base_vals)
    # calibrated by simulation (2026-10-13): pooled point estimate, sqrt(2) for a difference of two runs,
    # effect prior 1.5 x that: false-verified 0.7% under optional stopping at alpha 1%, power 74% at a
    # three-sigma effect with 5 seeds, 92% with 8
    sigma_d = math.sqrt(2.0) * sigma_upper(sd, df, 0.50)
    k = min(len(cand_vals), len(base_vals))
    diffs = [base_vals[i] - cand_vals[i] for i in range(k)] + [base_mean - c for c in cand_vals[k:]]
    gain = statistics.mean(diffs) if diffs else 0.0
    e_win = e_value(diffs, sigma_d, margin, tau=1.5 * sigma_d)
    e_stack = e_value(diffs, sigma_d, stackable_margin, tau=1.5 * sigma_d)
    w = verdict(cand_vals, base_vals, margin=margin, alpha=alpha, min_seeds=min_seeds, lower_is_better=True)
    out.update({"gain": round(gain, 5), "sd_single": round(sd, 5), "sd_diff_used": round(sigma_d, 5), "df": df,
                "e": round(e_win, 3), "e_stack": round(e_stack, 3), "p": w.get("p"), "t": w.get("t")})
    n = len(cand_vals)
    if gain <= 0:
        out["status"] = "fail"
    elif n < min_seeds or len(base_vals) < min_seeds:
        out["status"] = "promising"
    elif e_win >= 1.0 / alpha:
        out["status"] = "verified"
    elif e_stack >= 1.0 / stackable_alpha and sign_consistent is not False:
        out["status"] = "stackable"
    else:
        out["status"] = "close_call"
    return out


def futility(cand_vals: list[float], base_vals: list[float], lower_is_better: bool | None = None) -> bool:
    """Pre-declared early stop: after two seeds both worse than the baseline's own worst seed, stop
    (fail). Stopping for futility never inflates the false-verified rate."""
    cand_vals, base_vals = oriented(cand_vals, lower_is_better), oriented(base_vals, lower_is_better)
    if len(cand_vals) < 2 or not base_vals:
        return False
    return all(c > max(base_vals) for c in cand_vals[:2])
