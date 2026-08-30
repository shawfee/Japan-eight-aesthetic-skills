#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""同进程: 更新 8 个 SKILL.md 审计行 + 追加 test-results 进化章节 + 重新安装到 ~/.workbuddy/skills/。"""
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
STAMP = "100% (66/66 · darwin-evolve Gen3, 2026-08-30)"

def write_flush(p: Path, text: str):
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())

def copy_flush(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    with io.open(src, "rb") as fi, io.open(dst, "wb") as fo:
        while True:
            chunk = fi.read(1 << 20)
            if not chunk: break
            fo.write(chunk)
        fo.flush(); os.fsync(fo.fileno())

# 1) 更新审计行
for d in SKILL_DIRS:
    p = SKILLS / d / "SKILL.md"
    text = p.read_text(encoding="utf-8")
    if "待阶段 3 填充" in text:
        text = text.replace("待阶段 3 填充", STAMP, 1)
        write_flush(p, text)
        # 校验
        ok = STAMP in p.read_text(encoding="utf-8")
        print(f"[audit] {d}: {'updated' if ok else 'FAIL'}")
    else:
        print(f"[audit] {d}: 无占位符, skip")

# 2) 追加 test-results 进化章节
tr = BASE / "skills" / "test-results.md"
t = tr.read_text(encoding="utf-8")
add = """

## darwin evolve 自动进化 (Gen0 → Gen3, 2026-08-30)

在阶段 4 的 56 条规范探针之外, 扩展为 **66 条**(含 10 条对抗性混淆探针), 以独立盲测裁判做 ratcheting 自动进化:

| 代 | 通过率 | 关键编辑 |
|----|--------|----------|
| Gen0 基线 | 63/66 (95.5%) | — |
| Gen1 | 64/66 (97.0%) | parallel / ki 加边界诊断触发语 |
| Gen2 | 65/66 (98.5%) | micro 加 ce21 边界诊断触发语 |
| Gen3 | 66/66 (100%) | secret 反向信号 ce11 写进 frontmatter |

四处方编辑均落盘并校验; 整体通过率单调上升、零回退。详见 `EVOLUTION_LOG.md` 与 `eval/`。
"""
if "darwin evolve" not in t:
    t = t.rstrip() + "\n" + add
    write_flush(tr, t)
    print(f"[test-results] evolution section appended: {'OK' if 'darwin evolve' in tr.read_text(encoding='utf-8') else 'FAIL'}")
else:
    print("[test-results] already has evolution section, skip")

# 3) 重新安装到 ~/.workbuddy/skills/
for d in SKILL_DIRS:
    for fn in ("SKILL.md", "test-prompts.json"):
        src = SKILLS / d / fn
        dst = INSTALL / d / fn
        copy_flush(src, dst)
        same = src.read_bytes() == dst.read_bytes()
        print(f"[install] {d}/{fn}: {'synced' if same else 'MISMATCH'}")
print("DONE")
