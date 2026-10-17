"""N7: seeded contexts get seed words by abstract function and distance band, not a plain random draw.
Coverage of functions per part, a near/mid/far mix, no reuse on a part, determinism by run id, the random control."""
import os
import random
from collections import Counter
from types import SimpleNamespace

os.environ.setdefault("HTSA_LAB_ROOT", "D:/AGI-lab")

from nano import seeds as S  # noqa: E402


def _cat():
    cat = S.load_catalog()
    assert cat["seeds"], "harness/strategies/seeds/concepts_tagged.json is missing or empty"
    return cat


def test_catalog_covers_every_function_in_every_band():
    cat = _cat()
    have = {(r["function"], r["band"]) for r in cat["seeds"]}
    for f in S.FUNCTIONS:
        assert cat["hints"].get(f), f
        for b in ("near", "mid", "far"):
            assert (f, b) in have, (f, b)
    words = [r["word"] for r in cat["seeds"]]
    assert len(words) == len(set(words))


def test_functions_distinct_within_a_part():
    cat = _cat()
    for k in (1, 3, 5, 10):
        for trial in range(20):
            picks = S.choose("mix", k, set(), None, random.Random(f"r{trial}:{k}"), catalog=cat)
            assert len(picks) == k
            funcs = [p["function"] for p in picks]
            assert len(set(funcs)) == k, funcs
            assert all(p["hint"] for p in picks)


def test_distance_mix():
    cat = _cat()
    for trial in range(20):
        picks = S.choose("ffn", 4, set(), None, random.Random(f"d{trial}"), catalog=cat)
        bands = Counter(p["band"] for p in picks)
        assert bands["far"] == 2 and bands["mid"] == 1 and bands["near"] == 1, bands
        picks = S.choose("ffn", 2, set(), None, random.Random(f"e{trial}"), catalog=cat)
        bands = Counter(p["band"] for p in picks)
        assert bands["far"] == 1 and bands["far"] < 2, bands         # never all far, never all near
    # single contexts: over many parts and rounds roughly half far, the rest mid and near, all three present
    singles = Counter(S.choose("p", 1, set(), None, random.Random(i), catalog=cat)[0]["band"] for i in range(400))
    assert 150 < singles["far"] < 250 and singles["mid"] > 50 and singles["near"] > 50, singles


def test_used_seeds_excluded_on_the_part():
    cat = _cat()
    used: set = set()
    seen = []
    for rnd in range(6):
        picks = S.choose("opt", 5, used, None, random.Random(f"x{rnd}"), catalog=cat)
        words = [p["word"] for p in picks]
        assert not (set(words) & used), (rnd, set(words) & used)
        used |= set(words)
        seen += words
    assert len(seen) == len(set(seen))


def test_deterministic_by_seed_and_varies_across_runs():
    cat = _cat()
    a = S.choose("io", 5, set(), None, random.Random("seeds:runA:1:io:"), catalog=cat)
    b = S.choose("io", 5, set(), None, random.Random("seeds:runA:1:io:"), catalog=cat)
    c = S.choose("io", 5, set(), None, random.Random("seeds:runB:1:io:"), catalog=cat)
    assert a == b
    assert [p["word"] for p in a] != [p["word"] for p in c]


def test_history_shifts_function_weights():
    cat = _cat()
    hist = {"function": {"timing": {"sketches": 10, "clusters": 10}, "decay": {"sketches": 10, "clusters": 0}}}
    w = S.function_weights(hist)
    assert w["timing"] > w["flow"] > w["decay"] > 0         # every function keeps a chance
    first = Counter(S.choose("p", 1, set(), hist, random.Random(i), catalog=cat)[0]["function"] for i in range(600))
    assert first["timing"] > first["decay"]
    assert first["decay"] > 0


def test_yield_history_counts_distinct_clusters_per_function():
    info = {"hourglass": {"function": "timing"}, "metronome": {"function": "timing"}, "jar": {"function": "storage"}}
    sketches = [{"id": "s1", "card": "seeded", "seed": "hourglass"}, {"id": "s2", "card": "seeded", "seed": "metronome"},
                {"id": "s3", "card": "seeded", "seed": "jar"}, {"id": "s4", "card": "seeded", "seed": "jar"},
                {"id": "s5", "card": "formal", "seed": "jar"}]
    clusters = [{"cluster_id": "c1", "members": ["s1", "s3", "s4"]}, {"cluster_id": "c2", "members": ["s2", "s5"]}]
    h = S.yield_history(sketches, clusters, info)
    assert h["function"]["timing"] == {"sketches": 2, "clusters": 2}
    assert h["function"]["storage"] == {"sketches": 2, "clusters": 1}
    assert h["seed"]["jar"] == {"sketches": 2, "clusters": 1}


def test_prompt_line_names_the_function_only_for_tagged_seeds():
    seed = {"word": "hourglass", "function": "timing", "hint": "something that sets when things happen"}
    assert S.prompt_line(seed, "hourglass") == "Starting point: hourglass (timing: something that sets when things happen)"
    assert S.prompt_line(None, "anvil") == "Starting point: anvil"


def test_random_control_arm_is_the_old_draw():
    words = ["river", "lantern", "harbor", "glacier", "orchard"]
    rng_new, rng_old = random.Random("ctl"), random.Random("ctl")
    used_old: set = set()
    old = []
    for _ in range(4):
        w = rng_old.choice([x for x in words if x not in used_old] or words)
        used_old.add(w)
        old.append(w)
    new = S.choose("p", 4, set(), None, rng_new, mode="random", words=words)
    assert [p["word"] for p in new] == old
    assert all(not p["function"] for p in new)
    assert S.prompt_line(new[0], new[0]["word"]) == f"Starting point: {new[0]['word']}"


def _fake_loop(mode, tmp_path, run_id="b__nano__x__scaffold__r0"):
    from nano import loop as L
    tree = [{"id": "root"}, {"id": "mix"}, {"id": "ffn"}]
    obj = SimpleNamespace(seed_mode=mode, seed_info={}, seeds_by_part={}, seed_yield=[], used_seeds=set(),
                          sketches=[], clusters=[], decisions=[], run_id=run_id, run_dir=tmp_path, tree=tree)
    obj._part_of = lambda nid: nid if nid in ("mix", "ffn") else None
    obj._seed_for = lambda *a, **k: L.NanoLoop._seed_for(obj, *a, **k)
    return L, obj


def test_loop_assigns_distinct_functions_per_part(tmp_path):
    L, obj = _fake_loop("function", tmp_path)
    mix, ffn = {"id": "mix"}, {"id": "ffn"}
    specs = [("seeded", "anvil", mix, "inward"), ("formal", "rope", mix, "inward"), ("seeded", "bell", mix, "outward"),
             ("seeded", "kite", mix, "inward"), ("seeded", "cup", ffn, "inward")]
    out = L.NanoLoop._assign_seeds(obj, 1, specs)
    assert out[1] == specs[1]                                    # other cards keep their word
    mix_seeds = [obj.seed_info[sp[1]] for sp in out if sp[0] == "seeded" and sp[2] is mix]
    assert len({s["function"] for s in mix_seeds}) == 3
    assert (tmp_path / "seed_yield.json").exists()
    # round 2 never reuses a round-1 word on the same part
    out2 = L.NanoLoop._assign_seeds(obj, 2, specs)
    r1 = {sp[1] for sp in out if sp[2] is mix and sp[0] == "seeded"}
    r2 = {sp[1] for sp in out2 if sp[2] is mix and sp[0] == "seeded"}
    assert not (r1 & r2)
    # same run id, same picks
    _, obj2 = _fake_loop("function", tmp_path)
    assert L.NanoLoop._assign_seeds(obj2, 1, specs) == out


def test_loop_flag_parses():
    import subprocess
    import sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    r = subprocess.run([sys.executable, "-m", "nano.loop", "--help"], cwd=root, capture_output=True, text=True,
                       encoding="utf-8", env={**os.environ, "HTSA_LAB_ROOT": os.environ["HTSA_LAB_ROOT"]})
    assert "--seeds {function,random}" in r.stdout, r.stderr[-800:]
