#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""在同一进程内为 secret 的 frontmatter 补反向信号激活句, 写盘并立即校验。"""
import io, os
from pathlib import Path

p = Path(r"F:\WorkBuddy\2026-08-30-15-31-19\books\japan-eight-aesthetic-consciousness\skills\japan-secret-consciousness\SKILL.md")
old = '或场景涉及法律、安全、医疗等须准确传达的场域时,不调用本 skill。'
new = ('  或场景涉及法律、安全、医疗等须准确传达的场域时,不调用本 skill。'
       '但若用户说"读者没按我意思理解,要不要补解释/把话说尽",这恰是 秘 的反向信号(ce11)'
       '——应激活本 skill 施加"留入口而非继续补全"的边界, 而非判为不适用(除非涉及安全/责任须准确传达)。')

text = p.read_text(encoding="utf-8")
assert old in text, "old anchor not found!"
assert text.count(new) == 0, "already patched"
text = text.replace(old, new, 1)
# 写盘 + 强制刷缓冲
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(text)
    f.flush()
    os.fsync(f.fileno())

# 立即回读校验(同进程, 应看到自己的写入)
reread = p.read_text(encoding="utf-8")
ok = "反向信号(ce11)" in reread
print(f"[patch_secret] 写盘后同进程回读校验: {'PASS' if ok else 'FAIL'}")
print(f"[patch_secret] 含新句: {ok}")
