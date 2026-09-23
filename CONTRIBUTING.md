# 贡献与维护规则

这个仓库以个人面试学习为中心，新增内容应当服务于理解、练习、复盘或验证。

## 放置位置

- 解题思路、推导和错题记录放入 notes/。
- 主要服务于某篇笔记的动画与示例，放在对应专题目录中。
- 官方链接、题单、模式索引和稳定查阅资料放入 references/。
- 可复用的任务能力放入 skills/，并以 SKILL.md 作为入口。
- 有独立入口和使用流程的练习工具放入 apps/，同时提供局部 README。
- 项目级规则和学习路径放入 docs/。

## 新增 Skill

Skill 至少包含：

- 带有 name 和 description 的 SKILL.md frontmatter；
- 适用场景、工作流、输出要求和边界；
- 只有在确实需要时才添加 references、templates、scripts 或 examples。

## 新增 Reference

Reference 应说明类型、来源、访问日期、使用位置和许可边界。外部文章或题解只保留必要摘要与原始链接，不整篇复制。

## 提交前检查

~~~bash
git diff --check
find skills -name SKILL.md -print
~~~

涉及 HTML 时，打开对应页面完成一次最短交互检查，并在局部 README 中说明运行方式。
