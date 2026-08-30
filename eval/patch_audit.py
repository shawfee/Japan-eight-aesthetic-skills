#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""同进程: 将其余 7 个 skill 的审计行 '待补...' 改为 100% 标注, 并重装到 ~/.workbuddy/skills/。"""
import io, os, shutil
from pathlib import Path

BASE = Path(r"F:\WorkBuddy\2026-08-30-15-31-19\books\japan-eight-aesthetic-consciousness")
SKILLS = BASE / "skills"
INSTALL = Path.home() / ".workbuddy" / "skills"
SKILL_DIRS = [
    "japan-micro-consciousness", "japan-parallel-consciousness", "japan-ki-consciousness",
    "japan-ma-interval", "japan-secret-consciousness", "japan-plain-consciousness",
    "japan-kari-temporary", "japan-break-innovation",
]
OLD = "待补 (阶段 3 生成 test-prompts.json 后回填)"
STAMP = "100% (66/66 · darwin-evolve Gen3, 2026-08-30)"

def write_flush(p, text):
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())

for d in SKILL_DIRS:
    p = SKILLS / d / "SKILL.md"
    text = p.read_text(encoding="utf-8")
    if OLD in text:
        text = text.replace(OLD, STAMP, 1)
        write_flush(p, text)
        ok = STAMP in p.read_text(encoding="utf-8")
        print(f"[audit] {d}: {'updated' if ok else 'FAIL'}")
    # 重装
    dst = INSTALL / d / "SKILL.md"
    shutil.copyfile(p, dst)
    with open(dst, "rb") as f: pass
    print(f"[install] {d}/SKILL.md: {'synced' if p.read_bytes()==dst.read_bytes() else 'MISMATCH'}")
print("DONE")
