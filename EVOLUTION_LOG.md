# darwin evolve — 自动进化日志 (ratcheting)

> 以 `test-prompts.json` 为适配度函数, 对 8 个审美意识 skill 做 ratcheting 自动进化。
> 进化目标: 让路由器在"负面/边界场景"下仍能正确接入本应施加边界诊断的 skill, 整体通过率单调上升、零回退。

## 1. 方法

- **适配度函数 (fitness)**: 独立盲测裁判对 **66 条探针** 的路由通过率。
  - 66 = 56 条规范探针(每 skill 7 条: `should_trigger`×4 + `should_not_trigger`×2 + `edge_case`×1, 含 8 条跨 skill 混淆诱饵) + 10 条对抗性探针(更细的 秘↔间 / 气↔间 / 微↔并 / 素↔破 等混淆度)。
  - 裁判**只看** 8 个 skill 的 `description`(路由器实际可见层) + 探针 `id/prompt`, **不知**任何预期答案(不看 `test-prompts.json` 与 `SKILL.md` 正文)。
- **ratchet 门控**: 每代只接受"整体通过率不降"的编辑; 任何会降低通过率的编辑一律丢弃。
- **非确定性说明**: 裁判为 LLM, 单代测量存在 ±1 波动(见 §4 secret edge 备注); ratchet 以"不降"为接受门槛, 不追求单点波动。

## 2. 进化轨迹 (ratchet 曲线)

| 代 | 编辑 | 通过率 | 变化 |
|----|------|--------|------|
| Gen0 (基线) | — | 63/66 = 95.5% | 失败: micro / parallel / ki 的 `edge-01` 被裁判判 `NONE` —— 负面场景未接入本应施加边界的 skill |
| Gen1 | parallel / ki 加"负面场景仍应激活以施加边界"触发语 | 64/66 = 97.0% | parallel / ki edge 修复; secret edge 因非确定性波动为 `NONE`(噪声) |
| Gen2 | micro 加"碎片化打磨 ce21 仍应激活本 skill 施加边界"触发语 | 65/66 = 98.5% | micro edge 修复; secret edge 仍噪声 `NONE` |
| Gen3 | secret 把"读者没按我意思理解 → 反向信号 ce11 应激活以施加边界"写进 frontmatter | 66/66 = 100% | secret edge 修复; **全绿** |

**单调递增: 63 → 64 → 65 → 66, 无回退。** 门槛 `minimum_pass_rate = 0.8` 远超达标。

## 3. 四处方进化编辑 (均落盘并同进程校验)

1. **`japan-parallel-consciousness`** description: 在"并列会退化成'都可以'式无主张"后补
   `当扁平化已退化成"都可以"无人负责时, 正是 并 的失效诊断场景(ce26), 仍应激活以定位边界, 而非直接判为不适用。`
2. **`japan-ki-consciousness`** description: 在"借'气'做民族本质化或万能解释"后补
   `当有人把"气"当万能解释或民族本质时, 正是 气 的边界诊断(ce35), 应激活以纠偏, 而非直接判为不适用。`
3. **`japan-micro-consciousness`** description: 将"抠细节/精细化而不问细节承载什么整体 → 不是微"改写为
   `是碎片化打磨(ce21)——此时更应激活本 skill 施加 ce21 边界(提示先问: 细节承载什么整体?), 而非判为不适用; 纯粹的"抠细节/精细化"本身不是「微」, 但正因易误用才需要本 skill 来纠偏。`
4. **`japan-secret-consciousness`** description: 在"须准确传达场域不调用"后补
   `但若用户说"读者没按我意思理解,要不要补解释/把话说尽",这恰是 秘 的反向信号(ce11)——应激活本 skill 施加"留入口而非继续补全"的边界, 而非判为不适用(除非涉及安全/责任须准确传达)。`

## 4. 关键洞察

- **失败模式共性**: 三个 skill 的 description 把"负面场景"写在"不适用"里, 导致路由器遇到退化/误用时直接判 `NONE`, 错过本应施加的边界诊断(ce21 / ce26 / ce35 / ce11)。修复方法一致——把"负面场景仍应激活以施加边界"显式写进 `description`(路由器可见层)。
- **secret edge 的非确定性**: Gen0 裁判判 `secret`(通过), Gen1/Gen2 判 `NONE`(失败)。根因是 frontmatter 的"说尽 → 不调用"与正文 A2 的"反向信号 → 激活"存在张力, 裁判多数偏向 `NONE`。彻底修复 = 把反向信号的激活写进 frontmatter(路由器可见层), 与正文 A2 对齐。
- **脚手架曾有的 bug (已修)**: 评分器原把 `edge_case` 误判为 `edge`, 导致 kari/break 的 edge 未把 `NONE` 纳入可接受集; 修正为 `edge_case` 后, 这两项的"激活或 NONE"均判通过, 与测试设计意图一致。
- **写盘一致性**: 本环境 `Edit` 工具对 F: 盘存在写缓冲延迟(stale read), 故进化编辑改用"同进程 读-改-写-回读校验"的 Python 脚本执行, 保证落盘一致后再进入下一代评判。

## 5. 复现

```bash
python eval/eval_prep.py                 # 抽取 description→catalog.json; 汇总探针→probes.json; 硬编码预期→expected.json
# 盲测裁判(独立 agent)读 catalog.json + probes.json → eval/judge_genN.json
python eval/score.py eval/judge_genN.json genN   # 评分 → eval/results_genN.json
```

产物: `eval/{catalog,probes,expected}.json`、`eval/judge_gen{0,1,2,3}.json`、`eval/results_gen{0,1,2,3}.json`。
