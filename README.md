# GitHub Launch Kit

> 一个让 Codex 帮你把普通仓库打磨成“更适合公开发布、更容易被理解和收藏”的 skill。

[![Validate Skill](https://github.com/qqzxc276869-bot/github-launch-kit/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/qqzxc276869-bot/github-launch-kit/actions/workflows/validate-skill.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/qqzxc276869-bot/github-launch-kit?style=social)](https://github.com/qqzxc276869-bot/github-launch-kit/stargazers)

![GitHub Launch Kit 中文预览图](./preview.svg)

`github-launch-kit` 会让 Codex 用一套更偏实战的开源发布工作流，去优化一个仓库最影响第一印象的部分：项目定位、README 结构、快速上手路径、可信证据、以及发布文案。

它不追求“包装成爆款”，而是帮助一个本来就有价值的项目更容易被看懂、更容易被信任，也更容易被转发和点 star。

## 它解决什么问题

很多项目代码并不差，但 GitHub 首页很难让人产生行动：

- 项目一句话介绍太虚，10 秒内看不懂是做什么的
- README 一上来就在讲内部实现，而不是用户价值
- 顶部没有截图、GIF、输出示例、性能对比等证据
- Quickstart 太长，第一次尝试成本高
- 发布文案像营销口号，不像开发者之间会转发的内容

这个 skill 的目标，就是系统性地修这些问题。

## 为什么它更容易有传播性

大多数“帮仓库涨 star”的建议都很空泛，但这个 skill 是直接围绕仓库首页和发布动作落地的：

- 从现有仓库出发，而不是凭空写包装文案
- 优先处理清晰度、可信度、上手速度这三件最值钱的事
- 能直接改 README、补案例、改社区面，不停留在建议层
- 明确反对虚假数据、夸大表述和伪造热度

这让它特别适合独立开发者、小工具作者、AI agent 项目、脚本工具、模板仓库和 side project。

## 它能帮你做什么

- 打磨项目的一句话定位
- 诊断为什么仓库“有内容但不容易拿 star”
- 重写或重构 README
- 缩短首次上手路径
- 设计截图、GIF、对比图、基准测试等证据区
- 生成 GitHub、X、Reddit、Hacker News 的发布文案
- 补强 `CONTRIBUTING`、Issue 模板、PR 模板等社区面

## 效果示例

- 案例页：[docs/case-study.md](./docs/case-study.md)
- 演示素材方案：[docs/demo-assets-plan.md](./docs/demo-assets-plan.md)
- 发布文案包：[LAUNCH-COPY.md](./LAUNCH-COPY.md)

如果你正在准备公开发布，这三个文件会比单纯解释“这个 skill 是什么”更能帮助别人立刻理解它的价值。

## 示例提示词

```text
使用 $github-launch-kit 分析这个仓库为什么没人点 star，并给我直接可改的建议。
```

```text
使用 $github-launch-kit 重写这个项目的 README，让陌生用户 10 秒内看懂它的价值。
```

```text
使用 $github-launch-kit 把这个项目整理成适合发到 GitHub 和 Hacker News 的状态。
```

## 安装方式

把 `github-launch-kit/` 整个目录复制到 Codex 的 skills 目录：

```text
$CODEX_HOME/skills/github-launch-kit
```

然后显式调用：

```text
$github-launch-kit
```

## 仓库结构

```text
github-launch-kit/
  SKILL.md
  agents/openai.yaml
  references/
    launch-checklist.md
    readme-structure.md

docs/
  case-study.md
  demo-assets-plan.md
```

## 建议的仓库 Topics

发布到 GitHub 后，建议保留或接近以下 topics：

- `codex-skill`
- `github`
- `open-source`
- `developer-tools`
- `readme`
- `launch`
- `ai-agents`
- `prompt-engineering`
- `oss`

## 社区完善情况

这个仓库已经内置：

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- Bug report 模板
- Feature request 模板
- Pull request 模板
- 自动校验 workflow

这会让仓库从一开始就显得更完整，而不是“只有一个技能文件扔上来”。

## 接下来最值得补的内容

如果你还想继续提高收藏和转发概率，优先级最高的是：

1. 录一个 20 到 40 秒的 GIF，展示仓库改造前后对比
2. 补一个真实项目案例，说明这个 skill 改出了什么结果
3. 在首页顶部加一张“改造前 vs 改造后”的对比图

## 设计原则

这个 skill 的核心判断是：star 通常来自清晰度和信任，而不是夸张包装。

如果一个项目真正缺的是范围收敛、证据展示或示例质量，那么最好的做法是诚实地补这些内容，而不是只改几句更像广告的话。

## License

[MIT](./LICENSE)
