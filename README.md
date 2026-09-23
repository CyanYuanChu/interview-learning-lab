# Interview Learning Lab

面向技术面试的算法学习、主动回忆与小型实验仓库。

## 快速开始

1. 阅读 [二叉树解题框架](notes/algorithms/trees/hot100-binary-tree.md)。
2. 打开 [二叉树主动回忆测验](apps/hot100-binary-tree-quiz/index.html)。
3. 用 [Hot100 Recall](skills/hot100-recall/SKILL.md) 生成题目、评分和弱点复盘。
4. 需要新增内容时，先看 [目录规则](docs/repository-guide.md)。

本项目聚焦技术面试场景：算法理解、代码表达、边界判断和复盘闭环。

## 项目结构

| 目录 | 定位 | 入口 |
|---|---|---|
| notes/ | 个人解题笔记、思考过程和错题复盘 | [notes/README.md](notes/README.md) |
| references/ | 可追溯的题单、模式索引和稳定参考资料 | [references/README.md](references/README.md) |
| skills/ | 面向学习任务的 Agent Skills | [skills/README.md](skills/README.md) |
| apps/ | 可直接运行的交互式练习 | [apps/README.md](apps/README.md) |
| docs/ | 学习路径、维护规则和验证方法 | [docs/README.md](docs/README.md) |
| .specify/ | Spec Kit 项目工具和模板 | 工具目录 |
| .agents/、.claude/ | Agent 集成运行时目录 | 工具目录 |

## README、reference 和 skill 的区别

- README：导航、入口和使用方法。
- reference：来源明确、适合反复查阅的资料或索引。
- skill：面向特定任务的执行说明，入口文件始终是 SKILL.md。
- note：个人理解、推导、错误记录和解题过程。

## 当前 Skills

| Skill | 用途 |
|---|---|
| hot100-recall | 把题目和笔记转成主动回忆、评分与弱点复盘 |
| algorithm-visualizer | 设计可独立运行的算法状态演示 |
| repository-structure-audit | 检查目录边界、入口文件和 reference 元信息 |

## 本地运行

~~~bash
python3 scripts/serve.py
~~~

启动后在浏览器打开 `http://127.0.0.1:8765/apps/hot100-binary-tree-quiz/index.html`。在 Typora 中打开专题笔记时，也需要保持这个本地服务运行，以加载内嵌动画。

完整步骤见 [使用指南](docs/usage.md)。

## 维护入口

- [docs/learning-path.md](docs/learning-path.md)：面试学习顺序。
- [docs/validation.md](docs/validation.md)：提交前检查。
- [CONTRIBUTING.md](CONTRIBUTING.md)：新增笔记、reference、skill 和 app 的规则。
