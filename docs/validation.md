# 验证方法

## 文本与结构

~~~bash
git diff --check
find . -name '.DS_Store' -o -name '*.log'
find skills -name SKILL.md -print
~~~

检查结果应满足：

- 没有意外的空白错误；
- 没有把本地日志或系统元数据提交进仓库；
- 每个项目 skill 都有 SKILL.md。

## Skill

如果本机安装了 Codex skill creator，可以运行：

~~~bash
python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/hot100-recall
python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/algorithm-visualizer
python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/repository-structure-audit
~~~

## HTML Demo

~~~bash
open apps/hot100-binary-tree-quiz/index.html
~~~

至少检查页面能打开、题目导航可用、文本框可输入、进度能保存，以及答案包按钮能复制结果。
