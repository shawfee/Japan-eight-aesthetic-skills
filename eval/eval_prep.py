#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""darwin-evolve 评测脚手架:
1) 从 8 个 SKILL.md 抽取真实 description(路由器可见输入) -> catalog.json
2) 汇总 56 条规范探针 + 10 条对抗性探针 -> probes.json (gid 全局唯一)
3) 硬编码预期路由 -> expected.json
"""
import json, re, os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SKILLS = BASE / "skills"
EVAL = BASE / "eval"
EVAL.mkdir(exist_ok=True)

SKILL_DIRS = [
    "japan-micro-consciousness", "japan-parallel-consciousness", "japan-ki-consciousness",
    "japan-ma-interval", "japan-secret-consciousness", "japan-plain-consciousness",
    "japan-kari-temporary", "japan-break-innovation",
]

def extract_description(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return None
    fm = m.group(1)
    lines = fm.split("\n")
    out, capture = [], False
    for line in lines:
        if line.startswith("description:"):
            capture = True
            rest = line[len("description:"):].lstrip()
            if rest and rest != "|":
                out.append(rest)
            continue
        if capture:
            if line and not line[0].isspace() and line.rstrip().endswith(":"):
                break
            if line.strip() == "":
                continue
            out.append(line.strip())
    return " ".join(out).strip()

# 1) catalog
catalog = {}
for d in SKILL_DIRS:
    desc = extract_description(SKILLS / d / "SKILL.md")
    catalog[d] = desc
(EVAL / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[catalog] {len(catalog)} skills extracted")

# 2) probes (canonical 56)
probes = []
for d in SKILL_DIRS:
    tp = json.loads((SKILLS / d / "test-prompts.json").read_text(encoding="utf-8"))
    for c in tp["test_cases"]:
        probes.append({
            "gid": f"{d}::{c['id']}",
            "skill": d,
            "type": c["type"],
            "prompt": c["prompt"],
        })

# 对抗性探针 (10 条, 更细的混淆度)
adversarial = [
    ("adv-01", "japan-ma-interval", "should_trigger", "正文两侧要大片呼吸感留白,别挤满,让那片空本身能呼吸。"),
    ("adv-02", "japan-secret-consciousness", "should_trigger", "短视频结尾留悬念不揭晓,逼观众二刷自己拼图。"),
    ("adv-03", "japan-ki-consciousness", "should_trigger", "一进这空间就莫名压抑,说不出哪里不对,就是氛围不对。"),
    ("adv-04", "japan-micro-consciousness", "should_trigger", "别谈宏大战略了,先抓一个真实用户把他一天走完。"),
    ("adv-05", "japan-plain-consciousness", "should_trigger", "砍掉所有花哨特效,让素材自己说话。"),
    ("adv-06", "japan-kari-temporary", "should_trigger", "先用假数据搭个 demo 给老板验方向,定了再真做。"),
    ("adv-07", "japan-break-innovation", "should_trigger", "行业套路我学透了,现在要打破它的底层范式。"),
    ("adv-08", "japan-parallel-consciousness", "should_trigger", "三个部门各有一套流程,能不能都留着别强行统一?"),
    ("adv-09", "japan-secret-consciousness", "should_trigger", "教学时我不给标准答案,让学生自己推导出来。"),
    ("adv-10", "japan-ma-interval", "should_trigger", "对话节奏不对,该停的地方我还在灌。"),
]
for gid, skill, typ, prompt in adversarial:
    probes.append({"gid": f"adversarial::{gid}", "skill": skill, "type": typ, "prompt": prompt})

(EVAL / "probes.json").write_text(json.dumps(probes, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[probes] {len(probes)} total (canonical {len(probes)-len(adversarial)} + adversarial {len(adversarial)})")

# 3) expected
# 规范探针预期: should_trigger -> 本 skill; should_not_trigger -> 兄弟 skill 或 NONE; edge -> 本 skill
# 跨 skill 混淆诱饵(snt-01)的预期取自 test-prompts 的 expected_behavior 文本
SNT_MAP = {
    "japan-micro-consciousness::should-not-trigger-01": "japan-parallel-consciousness",
    "japan-parallel-consciousness::should-not-trigger-01": "japan-micro-consciousness",
    "japan-ki-consciousness::should-not-trigger-01": "japan-ma-interval",
    "japan-ma-interval::should-not-trigger-01": "japan-secret-consciousness",
    "japan-secret-consciousness::should-not-trigger-01": "japan-ma-interval",
    "japan-plain-consciousness::should-not-trigger-01": "japan-kari-temporary",
    "japan-kari-temporary::should-not-trigger-01": "japan-plain-consciousness",
    "japan-break-innovation::should-not-trigger-01": "japan-parallel-consciousness",
}
NONE_SNT = {
    "japan-micro-consciousness::should-not-trigger-02",
    "japan-parallel-consciousness::should-not-trigger-02",
    "japan-ki-consciousness::should-not-trigger-02",
    "japan-ma-interval::should-not-trigger-02",
    "japan-secret-consciousness::should-not-trigger-02",
    "japan-plain-consciousness::should-not-trigger-02",
    "japan-kari-temporary::should-not-trigger-02",
    "japan-break-innovation::should-not-trigger-02",
}
# edge 允许 NONE 的(反向信号/未守不破)
EDGE_ALLOW_NONE = {
    "japan-kari-temporary::edge-01",
    "japan-break-innovation::edge-01",
}
ADV_EXPECTED = {f"adversarial::{gid}": skill for gid, skill, _, _ in adversarial}

expected = {}
for p in probes:
    gid = p["gid"]; skill = p["skill"]; typ = p["type"]
    if gid in ADV_EXPECTED:
        expected[gid] = {"accept": [ADV_EXPECTED[gid]]}
    elif gid in SNT_MAP:
        expected[gid] = {"accept": [SNT_MAP[gid]]}
    elif gid in NONE_SNT:
        expected[gid] = {"accept": ["NONE"]}
    elif typ == "edge_case":
        acc = [skill] + (["NONE"] if gid in EDGE_ALLOW_NONE else [])
        expected[gid] = {"accept": acc}
    else:  # should_trigger
        expected[gid] = {"accept": [skill]}

(EVAL / "expected.json").write_text(json.dumps(expected, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[expected] {len(expected)} mapped")
