# 日本的八个审美意识 — Claude Skill 包

把黑川雅之《日本的八个审美意识》(1979) 蒸馏为 **8 个可复用 AI skill**，用 cangjie 拆书方法论（Adler 三阶段理解 + RIA++ + 三重验证 + 批判阶段）从扫描 PDF 全程自动化产出。本仓库即该方法论的完整产物与可复现脚手架，见 [GitHub 仓库](https://github.com/shawfee/Japan-eight-aesthetic-skills)。

> 这 8 个意识不是装饰美学，而是一组**可执行的判断/设计原则**：微、并、气、间、秘、素、假、破。每个 skill 都带"何时激活 / 何时判停 / 与兄弟意识如何区分 / 作者盲点边界"。

## 8 个 skill

| skill | 意识 | 一句话触发 |
|-------|------|-----------|
| `japan-micro-consciousness` | 微 | 复杂系统无从下手 → 从一个最小个体/当下瞬间入手，让整体从中浮现 |
| `japan-parallel-consciousness` | 并 | 多个对等主体如何共存而不设中心（扁平化/并列/去中心） |
| `japan-ki-consciousness` | 气 | 判断或营造空间/人际的"氛围、一体感、气场"（aura/atmosphere） |
| `japan-ma-interval` | 间 | 用留白/停顿/间距/余韵承载意义与节奏（negative-space / pacing） |
| `japan-secret-consciousness` | 秘 | 让对方自己想通/想进来，而非说尽说清楚（留白驱动想象） |
| `japan-plain-consciousness` | 素 | 做减法回到未加工本真，让素材而非造型说话 |
| `japan-kari-temporary` | 假 | 低依恋暂定原型 / 借来可弃 / 顺其自然（temporary / borrowed-form） |
| `japan-break-innovation` | 破 | 已精通规范后突破现状、引入突变（守破离 / break-the-rules） |

## 仓库结构

```
.
├── README.md
├── LICENSE                 # MIT + 原书引用说明
├── DIGEST.md               # 全书蒸馏总览(~7.4k 字)
├── INDEX.md                # 8 skill 关系图(mermaid) + 路由索引
├── GLOSSARY.md             # 22 条术语表(微/并/气/间/秘/素/假/破 + ce/g 编号)
├── BOOK_OVERVIEW.md        # 阶段0: Adler 三阶段 + 批判阶段(作者盲点)
├── STAGE1_CURATION.md     # 261 条候选方法论单元 → 8 意识分桶
├── verified.md             # 8 意识轻量验证(V1/V2/V3)
├── candidates/             # 5 类提取器产物(框架/原则/案例/反例/术语)
├── skills/                 # ★ 8 个 skill(SKILL.md + test-prompts.json)
│   ├── japan-*/SKILL.md
│   ├── japan-*/test-prompts.json
│   ├── SKILL_CATALOG.md    # 盲测目录(name+description+触发语)
│   └── test-results.md     # 阶段4 + darwin evolve 结果
├── EVOLUTION_LOG.md        # darwin evolve ratcheting 自动进化日志
├── eval/                   # 可复现的评测脚手架(catalog/probes/expected + scorer)
└── source_ocr.txt          # 扫描书 OCR 全文(溯源, 170 页去重)
```

## 安装

**WorkBuddy / Claude Code 用户级 skill 目录：**
```bash
# 把 8 个 skill 目录复制到 agent 的 skills 目录
cp -r skills/japan-* ~/.workbuddy/skills/        # WorkBuddy
# 或 cp -r skills/japan-* ~/.claude/skills/      # Claude Code
```
新装的 skill 在**下次对话**才出现在可用列表。

## 质量与自动进化（darwin evolve）

每个 skill 配 `test-prompts.json`（should_trigger / should_not_trigger / edge_case 三类，含跨 skill 混淆诱饵）。
以独立盲测裁判对 **66 条探针**（56 规范 + 10 对抗性）做 ratcheting 自动进化：

| 代 | 通过率 | 关键编辑 |
|----|--------|----------|
| Gen0 基线 | 63/66 (95.5%) | — |
| Gen1 | 64/66 (97.0%) | 并 / 气 加"负面场景仍应激活以施加边界"触发语 |
| Gen2 | 65/66 (98.5%) | 微 加 ce21 边界诊断触发语 |
| Gen3 | **66/66 (100%)** | 秘 反向信号 ce11 写进 frontmatter |

整体通过率单调上升、零回退。复现见 `EVOLUTION_LOG.md` 与 `eval/`。

## 引用与许可

- 原书：黑川雅之《日本的八个审美意识》（1979）。引文用于评论与教学，属合理引用。
- 本仓库的蒸馏产物（SKILL.md / DIGEST / GLOSSARY 等）采用 **MIT** 许可，详见 `LICENSE`。
