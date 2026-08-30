# 《日本的八个审美意识》· 索引

- **作者**:[日] 黑川雅之(Masayuki Kurokawa),工业/产品设计师,工学博士
- **出版**:日文原版约 2007 年,中文版中信出版社 2018 年 5 月
- **译者**:王超鹰、张迎星
- **一句话主旨**:微、并、气、间、秘、素、假、破——八种相互关联的审美意识,共同构成一种"尊重个体差异、留白、暂定与生成"的东方造物逻辑,它拒绝西方的普遍主义与统一哲学,却孕育出独特的卓越审美。

> 想先读精华长文,见 [DIGEST.md](DIGEST.md);术语查阅见 [GLOSSARY.md](candidates/glossary.md)。

---

## 八个 Skill(按八意识分组)

| # | 意识(slug) | 一句话作用 | 链接 |
|---|-----------|-----------|------|
| 1 | 微 `japan-micro-consciousness` | 从最小个体/当下瞬间入手,让整体从中浮现,而非先画全景再填空 | [SKILL.md](skills/japan-micro-consciousness/SKILL.md) |
| 2 | 并 `japan-parallel-consciousness` | 多个对等主体无中心、无主从地并列共存,靠看不见的联结维持和谐 | [SKILL.md](skills/japan-parallel-consciousness/SKILL.md) |
| 3 | 气 `japan-ki-consciousness` | 感知与营造空间/人际的一体感、氛围与气场领地(aura/atmosphere) | [SKILL.md](skills/japan-ki-consciousness/SKILL.md) |
| 4 | 间 `japan-ma-interval` | 设计由气构成的媒介性空隙——留白、停顿、间距、余韵与节奏 | [SKILL.md](skills/japan-ma-interval/SKILL.md) |
| 5 | 秘 `japan-secret-consciousness` | 主动不说尽,以留白与隐去驱动对方想象与共创(非保密) | [SKILL.md](skills/japan-secret-consciousness/SKILL.md) |
| 6 | 素 `japan-plain-consciousness` | 回到未加工本真,让素材而非造型说话,用形式限制激发创意 | [SKILL.md](skills/japan-plain-consciousness/SKILL.md) |
| 7 | 假 `japan-kari-temporary` | 以借来、暂定、可弃、融通无碍的低依恋心态做迭代与转化(仮≠偽) | [SKILL.md](skills/japan-kari-temporary/SKILL.md) |
| 8 | 破 `japan-break-innovation` | 在已"守"住范式后主动打破,借偶然与突变生成新范式(守破离) | [SKILL.md](skills/japan-break-innovation/SKILL.md) |

---

## 引用关系图(composes / contrasts)

实线 `composes` = 构成/支撑/前提关系;虚线 `contrasts` = 对照/相反相成关系。依据各 skill 的 `related_skills` 与"相关 skills"章节整理。

```mermaid
flowchart TB
    subgraph G["八意识 · 生成循环: 微→并→气/间→秘→素→假→破"]
        WEI["微 · 个体含整体"]
        HEI["并 · 去中心并列"]
        KI["气 · 一体氛围"]
        MA["间 · 媒介空隙"]
        HI["秘 · 不说尽"]
        SU["素 · 未加工本真"]
        KARI["假 · 暂借可弃"]
        HA["破 · 守后而破"]
    end

    WEI -->|composes: 微保证每块含整体且块间无中心| HEI
    WEI -->|composes: 视点(从哪看)| KI
    WEI -->|composes: 间的前提(先有个体才见间)| MA
    HEI -->|composes: 支撑并列的看不见联结| KI
    KI -->|composes: 间由气生| MA
    KI -->|composes: 素直/率真释气| SU
    MA -->|composes: 空隙即秘的入口,常叠加| HI
    SU -->|composes: 材质底座承载暂定| KARI
    KARI -->|composes: 融通无碍靠间落地| MA
    SU -->|composes: 破后归本| HA
    KARI -->|composes: 相反相成(假顺·破主动)| HA

    HEI -.->|contrasts: 求稳并列 vs 求变打破| HA
    WEI -.->|contrasts: 视点 vs 体感| KI
    WEI -.->|contrasts: 给个体 vs 给之间| MA
    HI -.->|contrasts: 对人(沟通) vs 对物(材质)| SU
    HI -.->|contrasts: 隐去邀补全 vs 放大见全体| WEI
    KARI -.->|contrasts: 顺势暂借 vs 主动否定| HA
```

---

## 推荐学习顺序

**微 → 并 → 气 → 间 → 秘 → 素 → 假 → 破**(一条从"基础关系"到"进阶生成"的自然递进)

1. **微**:一切的起点。先理解"个体中蕴含整体、个体即全体",否则后面的"间""并"都立不住——微是间的前提,也是并列关系里每一块独立单元的来源。
2. **并**:建立在微之上。微给出独立个体,并给出个体之间"无中心、无主从"的关系。先懂个体,才懂多个个体如何并列共存。
3. **气**:从"看什么"(微)走向"感觉到什么"(气)。气是氛围能量,也是支撑并列那道"看不见的联结"。理解了气,才接得住下面的"间"。
4. **间**:间由气生。必须先有气的延展与个体在场,才有所谓"间"。间是留白、停顿、节奏——把无形的关系变成可设计的空隙。
5. **秘**:间是容器,秘借容器驱动想象;二者常叠加(如松林图留白既是间也是秘的入口)。先会造"空",才会用"空"去邀对方共创。
6. **素**:回到未加工本真、让素材说话。素与秘的减法在不同维度(素对物、秘对人),且素为下一阶段的"假"提供材质底座。
7. **假**:建立在素之上(暂定的载体需有本真材质),又靠间落地(融通无碍靠流动空隙)。至此,"暂定、可弃、顺势"的空间与时间态度成形。
8. **破**:全书的终章与生成循环的闭合点。它要求先"守"住前七者(尤其素所回到的本真、假所打破的执念),才"破"得有意义;破靠素归本、与假相反相成,破后重启循环。

> 理由小结:这条顺序严格遵循书中的依赖关系——**微是前提、并是关系、气/间是无形媒介、秘是隐、素是本、假是暂、破是生**。每一步都为下一步提供支撑,最后"破"把循环重新打开。

---

## 关联文件

- [DIGEST.md](DIGEST.md) — 面向读者的精华长文(八意识分章 + 综括生成循环 + 反例陷阱 + 作者局限)
- [GLOSSARY.md](candidates/glossary.md) — 22 条关键术语词典(微/并/气/间/秘/素/假/破 等作者特殊用法)
- [BOOK_OVERVIEW.md](BOOK_OVERVIEW.md) — 全书骨架、术语与批判(阶段 0 产出)
- [verified.md](verified.md) — 八意识三重验证结论
- 案例与反例池:[cases.md](candidates/cases.md) · [counter-examples.md](candidates/counter-examples.md)
- 八个 skill 目录:[skills/](skills/)
