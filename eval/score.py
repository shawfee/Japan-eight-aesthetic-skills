#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""评分器: 读 judge 输出 (gid->choice) 与 expected.json, 计算通过率。
用法: python score.py <judge_json> <gen_label>
"""
import json, sys
from pathlib import Path
from collections import defaultdict

EVAL = Path(__file__).resolve().parent
expected = json.loads((EVAL / "expected.json").read_text(encoding="utf-8"))
probes = json.loads((EVAL / "probes.json").read_text(encoding="utf-8"))
judge_path = sys.argv[1]
gen = sys.argv[2] if len(sys.argv) > 2 else "gen0"
judge = json.loads(Path(judge_path).read_text(encoding="utf-8"))

# 归一化 choice
def norm(c):
    if c is None: return "NONE"
    c = c.strip()
    if c.lower() in ("none", "null", "无", "n/a", "-"): return "NONE"
    return c

results = []
per_skill = defaultdict(lambda: {"total": 0, "pass": 0, "fail": []})
for p in probes:
    gid = p["gid"]
    choice = norm(judge.get(gid))
    acc = expected[gid]["accept"]
    ok = choice in acc
    results.append({"gid": gid, "skill": p["skill"], "type": p["type"],
                    "prompt": p["prompt"], "choice": choice, "accept": acc, "pass": ok})
    per_skill[p["skill"]]["total"] += 1
    if ok: per_skill[p["skill"]]["pass"] += 1
    else: per_skill[p["skill"]]["fail"].append({"gid": gid, "choice": choice, "accept": acc})

total = len(results); passed = sum(1 for r in results if r["pass"])
print(f"\n===== {gen} 评分 =====")
print(f"整体通过率: {passed}/{total} = {passed/total*100:.1f}%")
print(f"{'skill':32} {'pass':>8} {'rate':>8}")
for s in sorted(per_skill):
    d = per_skill[s]
    rate = d["pass"]/d["total"]*100
    print(f"{s:32} {d['pass']:>3}/{d['total']:<3} {rate:>7.1f}%")
print("--- 失败项 ---")
for r in results:
    if not r["pass"]:
        print(f"  FAIL {r['gid']}  -> judge={r['choice']}  accept={r['accept']}")
        print(f"        prompt: {r['prompt']}")

out = {"gen": gen, "total": total, "passed": passed, "rate": passed/total,
       "per_skill": {s: {"total": d["total"], "pass": d["pass"],
                          "rate": d["pass"]/d["total"], "fail": d["fail"]} for s, d in per_skill.items()},
       "results": results}
(EVAL / f"results_{gen}.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\n[written] results_{gen}.json")
