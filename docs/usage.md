# 使用指南

## 本地启动

需要 Python 3，无需安装第三方依赖。在仓库根目录打开终端：

~~~bash
python3 scripts/serve.py
~~~

Windows 可以运行：

~~~powershell
py -3 scripts/serve.py
~~~

脚本会根据自身位置找到仓库，因此也可以从其他工作目录用脚本的完整路径启动。服务只监听本机 `127.0.0.1:8765`。保持终端运行；结束后按 `Ctrl+C` 停止。

如果端口已被占用，启动命令会显示错误地址和系统提示。笔记中的动画目前指向 `8765`；换端口时，也要将笔记 iframe 地址改为同一个端口。

## 浏览器练习

服务启动后，在浏览器打开：

~~~text
http://127.0.0.1:8765/apps/hot100-binary-tree-quiz/index.html
~~~

页面无需登录。作答进度保存在当前浏览器的本地存储中。

## Typora 动画笔记

1. 用 Typora 打开 `notes/algorithms/trees/hot100-binary-tree.md` 或 `notes/algorithms/graphs/hot100-graph-trie.md`。
2. 保持上面的本地服务运行，动画会通过 `http://127.0.0.1:8765/` 加载。
3. 点击动画中的播放、单步或重置控件，观察算法状态变化。

动画 HTML 与笔记都保存在仓库内。笔记也保留文字解释，方便不使用 Typora 或暂时没有启动服务时阅读。

## 使用项目 Skill

`skills/` 中的 Skill 是提供给 Codex、Claude 等 Agent 阅读的任务说明。向 Agent 提出任务时，可以指定相关文件。例如：

~~~text
请先阅读 skills/hot100-recall/SKILL.md，再根据
notes/algorithms/trees/hot100-binary-tree.md 给我做一次主动回忆练习。
一次问一道题，等我回答后再继续。
~~~

更多任务入口见 [Skills 索引](../skills/README.md)。
