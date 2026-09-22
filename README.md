# Interview Learning Lab

面试算法学习、三语言模板、交互式演示和 Agent Skills 的个人学习仓库。

## 当前状态

这是项目初始化阶段。当前内容仍保留在根目录，完整的目标结构和迁移顺序见 [plan.md](plan.md)。

已经完成：

- 清理旧的 Typora/HTTP 临时入口；
- 增加根目录 .gitignore；
- 保留二叉树学习笔记和主动回忆测验；
- 按要求移除 Hot 100 总复习稿、三语言模板和路径总和演示；
- 已初始化本地 Git 仓库，默认分支为 main；
- 已创建公开 GitHub 仓库：[CyanYuanChu/interview-learning-lab](https://github.com/CyanYuanChu/interview-learning-lab)；
- 本地 `main` 已推送并跟踪 `origin/main`。

## 现在可以查看的内容

| 文件 | 用途 |
|---|---|
| [hot100_binary_tree.md](hot100_binary_tree.md) | 二叉树统一解题框架和题型模板 |
| [hot100_binary_tree_quiz.html](hot100_binary_tree_quiz.html) | 二叉树主动回忆测验 |
| [plan.md](plan.md) | 项目目录、README、reference、skills 和迁移计划 |

## 本地打开演示

在 macOS Finder 或终端中直接打开：

~~~bash
open hot100_binary_tree_quiz.html
~~~

浏览器交互行为尚未在本次初始化中重新做完整 smoke check；后续会在 apps/ 结构迁移后补验证。

## 目录约定

目标结构会把内容分为：

- notes/：个人学习笔记和推导；
- references/：外部来源、稳定模板和事实索引；
- skills/：每个能力以 SKILL.md 为入口的 Agent Skills；
- apps/：可运行的学习实验和交互工具；
- docs/：项目级说明、学习路线和验证手册；
- .specify/、.agents/、.claude/：规划工具和 Agent 集成运行时。

## 规划与后续

Phase 0 的本地与 GitHub 初始化已经完成。之后按 [plan.md](plan.md) 进入目录 README、内容迁移和第一批 skills 的实现。
