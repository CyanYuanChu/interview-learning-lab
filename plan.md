# Interview Learning Lab 项目结构计划

> 状态：Draft，等待确认后执行
> 项目根目录：`/Users/cyan/workspace/Interview`
> 日期：2026-09-22
> 本阶段范围：建立结构设计、完成本地项目初始化，并清理已确认的临时文件；有价值的学习内容暂不移动、不改写。

## 1. 项目定位

将当前目录整理成一个可持续维护的「面试学习实验室」项目，统一容纳：

- 算法与数据结构学习笔记；
- Java / C++ / Python 三语言对照模板；
- 可在浏览器中运行的交互式演示；Typora 集成作为未来可选扩展；
- 可复用的 Agent Skills 及其参考资料、模板和脚本；
- 外部资料索引与来源说明；
- 后续可独立运行的学习应用；
- 项目级规划、验证和贡献规范。

项目暂定名为 **Interview Learning Lab**。根目录仍沿用当前的 `Interview`，暂不新建第二层项目目录。

## 2. 当前目录盘点（已验证）

当前根目录已经有 `README.md`、`.gitignore`，本地 Git 仓库也已经初始化为 `main` 分支但尚无提交；学习内容仍暂时保留在根目录。现有内容是三种东西混合在一起：

| 当前路径 | 当前角色 | 计划中的归类 |
|---|---|---|
| `README.md` | 项目入口和当前状态说明 | 保留在根目录 |
| `.gitignore` | 忽略 macOS 元数据、构建产物和本地环境 | 保留在根目录 |
| `.git/` | 本地 Git 历史和分支元数据 | 保留，不提交其内部文件 |
| `hot100_binary_tree.md` | 二叉树题型框架和递归模板 | `notes/algorithms/trees/hot100-binary-tree.md` |
| `hot100_binary_tree_quiz.html` | 可运行的二叉树主动回忆测验 | `apps/hot100-binary-tree-quiz/index.html` |
| `hot100_review.md`、`hot100_3lang_templates.md`、`path-sum-count-bug.html` | 已按用户要求移入废纸篓 | 不纳入当前项目结构 |
| `path-sum-http.md`、`typora-iframe-test.md` | 已确认是旧的 Typora/HTTP 测试入口，已移入废纸篓 | 不再作为当前项目内容 |
| `typora-embed-demo/*` | 已被用户删除，当前 checkout 中不存在 | 不恢复，不纳入当前项目结构 |
| `.specify/*` | Spec Kit 的项目工具、模板和脚本 | 保留，归入“项目工具层”，不当作学习资料 |
| `.agents/skills/*`、`.claude/skills/*` | 当前 Spec Kit 集成产生的 skill 运行时文件 | 保留，后续与项目自有 skills 分开管理 |
| `.DS_Store` | macOS 工作区元数据，已移入废纸篓 | 通过 `.gitignore` 防止再次进入项目 |

### 2.1 已执行的安全清理（2026-09-22）

- 将根目录的 `.DS_Store` 移入 macOS 废纸篓；
- 将 `path-sum-http.md` 移入废纸篓：它依赖已经删除的 Typora demo 入口；
- 将 `typora-iframe-test.md` 移入废纸篓：它指向外部 Codex 会话产物，不属于当前项目内容；
- 保留 `hot100_binary_tree.md` 和 `hot100_binary_tree_quiz.html`，它们仍是当前有效学习内容；
- 按用户要求移除 `hot100_review.md`、`hot100_3lang_templates.md` 和 `path-sum-count-bug.html`，文件仍可从 macOS 废纸篓恢复。

### 2.2 GitHub 初始化状态

- GitHub 账号已确认：`CyanYuanChu`；
- 本地 Git 已初始化，使用 `main` 作为默认分支，当前尚无提交；
- 提交身份尚未配置，不会擅自写入或公开个人邮箱；
- 远程仓库名称、可见性和是否创建 GitHub README 等待用户确认；
- 远程创建后设置 `origin`，完成首个提交并推送；
- 不使用 GitHub 自动生成 README，避免与当前本地 README 冲突。

当前目录中没有 `hot100-site/`。历史工作记录提到过独立的 Hot 100 Web 应用，但它不在本次实际盘点到的 checkout 中；本计划不凭空创建或迁移它。若日后恢复，应作为 `apps/hot100-site/` 独立子项目接入，并单独补充 README、环境变量和部署说明。

## 3. 设计原则

### 3.1 README 是入口和导航，不是资料仓库

- 根目录 `README.md` 只回答：项目是什么、从哪里开始、目录怎么分、如何运行演示、有哪些 skills 和参考资料。
- 只有需要独立运行或独立维护的模块才放局部 README。
- README 负责索引和操作说明；详细知识内容放到 `notes/` 或 `references/`。
- 每个局部 README 都要说明输入、启动命令、预期结果和验证方式。

### 3.2 明确区分 notes、docs、references、skills

| 目录 | 用途 | 可以包含什么 | 不应该包含什么 |
|---|---|---|---|
| `notes/` | 个人学习内容和推导 | 题解、思考过程、易错点、复盘 | 外部资料的整篇复制 |
| `docs/` | 项目级说明和操作手册 | 学习路线、贡献规范、运行手册、架构说明 | 面向某个题目的大量题解 |
| `references/` | 可追溯的参考资料 | 官方链接、模板、术语表、来源映射、许可证信息 | 没有来源的“权威结论” |
| `skills/` | Agent 可复用的任务能力 | `SKILL.md`、按需加载的 references、脚本、模板、示例 | 把个人笔记直接伪装成 skill |
| `apps/` | 可运行的实验和工具 | HTML、前端应用、服务脚本、运行说明 | 仅用于解释概念的长篇笔记 |
| `specs/` | Spec Kit 的功能级规划历史 | `spec.md`、`plan.md`、`tasks.md` 等 | 项目日常学习笔记 |

### 3.3 Skill 采用“入口文件 + 按需资源”

每个 skill 目录至少包含：

~~~text
skills/<skill-name>/
├── SKILL.md                 # 必需：元数据、触发条件、工作流和输出格式
├── references/              # 可选：只有需要时才读取的长文档
├── templates/               # 可选：生成结果的起始模板
├── scripts/                 # 可选：确定性、可重复执行的辅助脚本
└── examples/                # 可选：最小输入与期望输出
~~~

`SKILL.md` 只保留任务入口和关键约束；较长的背景资料下沉到 `references/`，避免每次触发都加载全部内容。skill 的资源引用必须使用相对路径，不得写入密钥或用户私密数据。

### 3.4 可运行内容必须自描述

每个 `apps/<name>/` 都需要自己的 README，至少包含：

1. 这个演示解释了什么；
2. 是否需要本地 HTTP 服务；
3. 完整启动命令；
4. 访问地址或打开方式；
5. 已验证和未验证的边界；
6. 停止服务的方式。

## 4. 目标目录结构

以下是目标蓝图。第一阶段不要求一次性创建所有空目录，只创建有内容或有明确入口的目录。

~~~text
Interview/
├── README.md                         # [README] 项目总入口、导航、快速开始
├── plan.md                           # [PLAN] 本仓库级结构蓝图（当前文件）
├── CONTRIBUTING.md                   # [DOC] 如何新增笔记、reference、skill、demo
├── LICENSE                           # [META] 待确认：个人代码与外部资料的许可策略
├── .gitignore                        # [META] 忽略 .DS_Store、构建产物、密钥和本地状态
│
├── docs/                             # [DOCS] 项目级说明，不承载题目正文
│   ├── README.md                     # [README] 文档导航和阅读顺序
│   ├── learning-path.md              # 学习路线：算法、语言、复盘、可视化
│   ├── repository-guide.md           # 目录边界、命名和新增文件规则
│   └── validation.md                 # Markdown、链接、demo、skill 的验证方法
│
├── notes/                            # [NOTES] 个人学习笔记和推导
│   ├── README.md                     # [README] 笔记分类和写作约定
│   └── algorithms/
│       ├── README.md                 # [README] 算法专题索引
│       └── trees/
│           └── hot100-binary-tree.md  # hot100_binary_tree.md 的归档位置
│
├── references/                       # [REFERENCE] 外部来源、稳定模板和事实索引
│   ├── README.md                     # [README] reference 的来源、状态和使用规则
│   ├── algorithms/
│   │   └── pattern-index.md           # 滑动窗口、双指针、树、前缀和等模式索引
│   └── external/
│       └── leetcode-hot100.md         # 外部题单、链接、访问日期和备注
│
├── skills/                           # [SKILLS] 项目自有、可复用的 Agent 能力
│   ├── README.md                     # [README] skill 目录、触发词和资源说明
│   ├── hot100-recall/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   ├── review-format.md
│   │   │   └── mistake-taxonomy.md
│   │   ├── templates/
│   │   │   └── question.md
│   │   └── examples/
│   ├── language-bridge/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── java-cpp-python-map.md
│   ├── algorithm-visualizer/
│   │   ├── SKILL.md
│   │   └── templates/
│   └── repository-structure-audit/
│       └── SKILL.md
│
├── apps/                             # [APPS] 可运行的学习实验和交互工具
│   ├── README.md                     # [README] 应用/演示索引
│   ├── hot100-binary-tree-quiz/
│   │   ├── README.md
│   │   └── index.html                # hot100_binary_tree_quiz.html
│   └── <future-app>/                 # 只有恢复新的交互项目后再添加
│
├── scripts/                          # [SCRIPTS] 跨模块的确定性工具
│   └── README.md                     # 只有出现共用脚本后再扩展
│
├── tests/                            # [TESTS] 可自动化的 smoke、结构和演示验证
│   └── README.md
│
├── specs/                            # [SPEC-KIT] 未来的功能级规划历史
│   └── <feature-id>/
│       ├── spec.md
│       ├── plan.md
│       ├── research.md
│       ├── data-model.md
│       ├── quickstart.md
│       └── tasks.md
│
├── .github/                          # [GITHUB] CI、Issue/PR 模板（后续阶段）
│   └── workflows/
│
├── .specify/                         # [TOOLING] Spec Kit 运行时和模板，保留原样
├── .agents/                          # [TOOLING] 当前 Agent 集成运行时，保留并单独说明
└── .claude/                          # [TOOLING] Claude 集成兼容目录，保留并单独说明
~~~

### 4.1 README 清单

必须创建或保留的 README：

| README | 责任 |
|---|---|
| 根目录 `README.md` | 让第一次打开仓库的人在 3 分钟内理解项目并跑通一个 demo |
| `docs/README.md` | 说明文档阅读顺序和维护范围 |
| `notes/README.md` | 说明笔记如何按专题组织 |
| `references/README.md` | 说明什么算 reference、如何记录来源和许可证 |
| `skills/README.md` | 列出每个 skill 的用途、触发词、入口和资源 |
| `apps/README.md` | 列出所有可运行 demo 及其启动方式 |
| 每个独立 app 的 `README.md` | 只描述该 app 的运行、验证和边界 |

不要求为每一个 Markdown 笔记都创建 README；用父目录 README 做索引即可。

### 4.2 Reference 文件判定规则

一个文件进入 `references/`，需要满足至少一项：

- 它记录了外部官方资料、题单或规范的链接和访问日期；
- 它是多个笔记或 skill 共用的稳定模板、术语表或映射表；
- 它的主要价值是“查阅”，而不是记录一次个人思考过程。

每个 reference 文档使用统一元信息：

~~~markdown
# 标题

- 类型：官方文档 / 题单 / 模板 / 术语表
- 来源：[名称](URL)
- 访问日期：YYYY-MM-DD
- 使用位置：列出引用它的 notes、skills 或 apps
- 许可说明：如适用，说明是否只保留摘要和链接
~~~

外部文章、题解和课程不整篇复制；项目只保留必要摘要、自己的理解和原始链接。

## 5. 第一批 Skills 设计

### 5.1 `hot100-recall`

用途：把 Hot 100 笔记、个人易错点和题目状态转换成主动回忆题、快速复盘卡片或复习报告。

必须遵守：

- 每道题先输出一句话知识点；
- 显式区分已从个人代码/提交确认的易错点与通用风险；
- 需要代码时同时提供 Java、C++、Python 的对应表达；
- 题型和评分标准可追溯到 `skills/hot100-recall/references/`。

### 5.2 `language-bridge`

用途：把一个算法模板拆成 Java、C++、Python 的语法、容器、边界和复杂度对照。

必须遵守：

- 先解释公共算法不变量，再解释语言差异；
- 不为了“看起来不同”而制造无意义的改写；
- 对整数溢出、容器默认行为、索引边界和排序比较器给出明确提醒。

### 5.3 `algorithm-visualizer`

用途：把算法状态机或边界变化生成可独立运行的 HTML 演示，并提供浏览器预览说明。

必须遵守：

- HTML、CSS、JavaScript 默认自包含；
- 不把脚本塞进 Markdown；
- 涉及本地预览时明确访问方式、端口、停止方式和“已验证/未验证”范围；
- 视觉演示不能替代代码和不变量解释。

### 5.4 `repository-structure-audit`

用途：检查新增文件是否放入正确的 notes、references、skills、apps、docs 边界，并更新索引。

必须遵守：

- 报告未分类的根目录文件；
- 检查 skill 是否有合法的 `SKILL.md` 元数据；
- 检查 reference 是否包含来源元信息；
- 不自动移动或删除用户文件，只给出建议或经过确认后执行。

## 6. 实施阶段

### Phase 0：确认边界与仓库基础设施

- 确认项目名、是否公开、许可证策略；
- 初始化本地 Git 仓库，使用 `main` 分支并创建首个初始化提交；
- 创建 GitHub 个人仓库，设置 `origin` 并推送首个提交；
- 创建 `.gitignore`，至少忽略 `.DS_Store`、构建产物、本地服务状态、环境变量和密钥；
- 明确 `.specify/`、`.agents/`、`.claude/` 是工具层，不与学习资料混排；
- 不把历史上不在当前 checkout 的应用当成本阶段输入。

### Phase 1：创建入口文档和分类索引

- 根目录 `README.md` 已创建；
- 创建 `docs/README.md`、`notes/README.md`、`references/README.md`、`skills/README.md`、`apps/README.md`；
- 把本计划中的当前文件映射表转成 README 中可维护的导航；
- 创建 `CONTRIBUTING.md`，约束新增文件应该落在哪一层。

### Phase 2：迁移现有内容

- 先复制/移动到目标目录，再逐条修复相对链接；
- 仅在链接和 demo 入口验证通过后删除旧位置；
- 将根目录的长篇笔记和 HTML demo 清出根目录；
- 保留原始内容语义，不在迁移阶段顺手重写算法结论；
- 迁移后重新确认每个 HTML demo 的入口和本地预览路径。

### Phase 3：实现第一批 skills

- 先实现 `hot100-recall` 和 `language-bridge`；
- 再实现 `algorithm-visualizer` 和 `repository-structure-audit`；
- 每个 skill 先有最小 `SKILL.md`，再按需增加 reference、template、script；
- 为每个 skill 提供一个最小示例和一个失败边界说明。

### Phase 4：验证与维护自动化

- 检查 README、Markdown 和 reference 的相对链接；
- 检查每个 app 的启动命令和端口说明；
- 对 HTML demo 做最短真实浏览器 smoke check；
- 检查 skill frontmatter、相对资源链接和脚本帮助信息；
- 后续再考虑 GitHub Actions、自动目录索引和发布。

## 7. 验收标准

完成结构迁移后，应满足：

- 根目录 README 能指向所有一级内容目录，并明确哪些是 README、哪些是 reference、哪些是 skill；
- 根目录不再散落未分类的长篇笔记或 demo（`README.md`、`plan.md` 和工具配置除外）；
- 当前盘点出的每个用户文件都有唯一目标位置，没有静默丢失；
- 每个可运行 demo 都有局部 README、启动命令和停止方式；
- 每个 skill 都有 `SKILL.md`，并把长资料放在明确的 `references/` 下；
- 每个项目级 reference 都能追溯到来源、访问日期和许可边界；
- README 中不承诺未实际验证的部署、模型评分或浏览器行为；
- 不提交 `.DS_Store`、密钥、本地环境变量和构建产物；
- 后续功能规划使用 `specs/<feature-id>/`，不把功能 plan 和本仓库级 `plan.md` 混为一谈。

## 8. 本阶段不做的事

- 不在没有确认仓库名和可见性前创建 GitHub 远程仓库；
- 不再重复清理已经移入废纸篓的旧 Typora 文件；
- 不恢复当前目录中不存在的 `hot100-site`；
- 不把外部 GitHub skill 或文章整包复制进项目；
- 不新增 Web 后端、数据库、登录、部署或模型 API；
- 不把一次性的个人复盘内容直接提升为通用 skill。

## 9. 结构设计参考

本计划吸收以下公开项目的可迁移做法：

1. [anthropics/skills](https://github.com/anthropics/skills)：每个能力以独立目录组织，入口是 `SKILL.md`，大型资料按需放入 `references/`，并使用渐进式加载。
2. [github/awesome-copilot](https://github.com/github/awesome-copilot)：把 skills、agents、instructions、脚本和校验规范分成不同层次；项目级 skill 需要清晰元数据和资源引用。
3. [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)：把算法内容、tests、scripts、README、CONTRIBUTING 和生成/索引文件分开，根 README 负责入口和导航。
4. [ossu/computer-science](https://github.com/ossu/computer-science)：用根 README 组织学习路径，并把额外阅读材料放入独立的 `extras/readings` 体系，而不是混进主课程正文。
5. [github/spec-kit](https://github.com/github/spec-kit)：保留工具运行时与产品内容的边界；本项目的 `.specify/` 是工具层，未来功能级规格放入独立的 `specs/<feature-id>/`。

## 10. 后续执行入口

本文件确认后，下一步按以下顺序执行：

1. 确认 GitHub 仓库名、公开/私有属性和许可证策略；
2. 初始化本地 Git，创建首个提交并推送到 `origin`；
3. 创建五个一级目录 README；
4. 迁移现有文件并验证链接；
5. 创建第一批 skills；
6. 做一次结构审计和真实 demo smoke check；
7. 再决定是否接入 CI。

本文件是仓库级结构计划。未来使用 Spec Kit 规划具体功能时，仍应为每个功能单独创建 `specs/<feature-id>/spec.md` 和 `specs/<feature-id>/plan.md`。
