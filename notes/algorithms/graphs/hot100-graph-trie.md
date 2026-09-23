# Hot 100 图论与 Trie：四题统一解题框架

本笔记整理四道很有代表性的题：

- 200. 岛屿数量：网格连通块
- 994. 腐烂的橘子：多源 BFS + 分层计时
- 207. 课程表：有向图环检测 + 拓扑排序
- 208. 实现 Trie（前缀树）：用树保存字符串前缀

代码以 Java 为主，代码块默认已经导入 java.util.*；图解使用 ASCII、Mermaid 和可点击的 Typora 动画。动画依赖本机的回环地址 http://127.0.0.1:8765/。

---

## 一、四道题其实在考什么

~~~mermaid
flowchart LR
    A["网格"] --> B["200 岛屿数量"]
    C["扩散过程"] --> D["994 腐烂的橘子"]
    E["有向图"] --> F["207 课程表"]
    G["字符串前缀"] --> H["208 Trie"]
~~~

| 题目 | 数据结构 | 核心算法 | 最关键的状态 |
| --- | --- | --- | --- |
| 200 岛屿数量 | 二维网格 | DFS / BFS / 并查集 | 哪些陆地已经访问 |
| 994 腐烂的橘子 | 二维网格 + 队列 | 多源 BFS | 当前分钟有哪些腐烂橘子 |
| 207 课程表 | 邻接表 | Kahn BFS / DFS 染色 | 入度或节点访问状态 |
| 208 Trie | 多叉树 | 沿字符走树 | 当前前缀是否存在、是否完整单词 |

### 看到题目时先问四个问题

1. **状态是什么？** 是网格、节点、边，还是字符串前缀？
2. **相邻关系是什么？** 网格通常是上下左右；图题由边决定；Trie 的相邻节点由字符决定。
3. **访问过的状态怎么标记？** 可以修改原数组，也可以使用 visited、颜色数组或集合。
4. **什么时候算完成？** 扫完所有格子、队列清空、所有课程出队，或者走到单词结尾。

一句话记忆：

> DFS 是“沿一条路走到底”，BFS 是“按距离一层一层扩散”，并查集是“把相连的点合成集合”，Trie 是“每个字符沿一条边向下走”。

---

## 二、200. 岛屿数量

### 1. 题意

1 表示陆地，0 表示水。上下左右相连的陆地属于同一个岛屿，返回岛屿数量。

例如：

~~~text
1 1 0 0 0
1 1 0 1 0
0 0 0 1 1
~~~

左边四个 1 是一个岛，右边三个 1 是另一个岛，所以答案是 2。

### 2. DFS 图解：发现一个岛，就把整座岛淹掉

~~~text
初始：
1 1 0 0 0
1 1 0 1 0
0 0 0 1 1

扫描到左上角 1：
count = 1

DFS 访问整块陆地，把访问过的 1 改成 0：
0 0 0 0 0
0 0 0 1 0
0 0 0 1 1

继续扫描，找到右侧第一块陆地：
count = 2
~~~

~~~mermaid
flowchart TD
    A["扫描到一个未访问的 1"] --> B["岛屿数量 + 1"]
    B --> C["DFS 进入上下左右"]
    C --> D["遇到 1 就标记为 0"]
    D --> E["整块连通陆地被访问"]
    E --> F["继续扫描网格"]
~~~

<iframe
  src="http://127.0.0.1:8765/notes/algorithms/graphs/islands.html"
  width="100%"
  height="650"
  title="200 岛屿数量 DFS 淹岛动画"
  loading="eager"
  style="border:0; border-radius:16px;">
</iframe>

关键点不是“每个 1 都加一”，而是：

> 只有发现一块新陆地时加一；进入这块陆地后，把所有相连的陆地一次性访问完。

### 3. Java：DFS 原地标记

~~~java
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;
        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j, m, n);
                }
            }
        }

        return count;
    }

    public void dfs(char[][] grid, int r, int c, int m, int n) {
        if (r < 0 || r >= m
                || c < 0 || c >= n
                || grid[r][c] != '1') {
            return;
        }

        // 标记访问过，避免重复进入
        grid[r][c] = '0';

        dfs(grid, r + 1, c, m, n);
        dfs(grid, r - 1, c, m, n);
        dfs(grid, r, c + 1, m, n);
        dfs(grid, r, c - 1, m, n);
    }
}
~~~

### 4. Java：BFS 写法

DFS 和 BFS 的“淹岛”逻辑完全一样，只是一个用递归栈，一个用队列。

~~~java
class Solution {
    private static final int[][] DIRS = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;
        Queue<int[]> queue = new ArrayDeque<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] != '1') {
                    continue;
                }

                islands++;
                grid[r][c] = '0';
                queue.offer(new int[]{r, c});

                while (!queue.isEmpty()) {
                    int[] cell = queue.poll();

                    for (int[] dir : DIRS) {
                        int nr = cell[0] + dir[0];
                        int nc = cell[1] + dir[1];

                        if (nr >= 0 && nr < rows
                                && nc >= 0 && nc < cols
                                && grid[nr][nc] == '1') {
                            grid[nr][nc] = '0';
                            queue.offer(new int[]{nr, nc});
                        }
                    }
                }
            }
        }

        return islands;
    }
}
~~~

### 5. 并查集思路

把每个陆地看成一个集合：

~~~text
初始：每个陆地各自为一个集合

1 —— 1       1 —— 1 —— 1
│             │
1             1

合并后：这些陆地属于同一个连通分量
~~~

做法：

1. 每个 1 初始贡献一个岛屿；
2. 遇到相邻的两个 1，执行 union；
3. 两个集合第一次合并成功时，岛屿数量减一。

并查集适合需要频繁回答“两个点是否连通”的场景；本题用 DFS/BFS 更直接。

### 6. 复杂度与易错点

- DFS / BFS：时间 O(m × n)；
- 原地把 1 改成 0 时，递归栈或队列最坏 O(m × n)；
- 如果不能修改 grid，使用 visited，空间 O(m × n)；
- 必须在入队或递归进入时立即标记，否则同一个格子可能重复访问；
- 不能只看左边和上边，岛屿会向四个方向连接。

---

## 三、994. 腐烂的橘子

### 1. 题意

- 0：空
- 1：新鲜橘子
- 2：腐烂橘子

每分钟，腐烂橘子会让上下左右的新鲜橘子腐烂。返回让所有橘子腐烂需要的最少分钟数；如果有橘子永远无法腐烂，返回 -1。

### 2. 为什么是多源 BFS

一开始所有腐烂橘子都应该同时开始扩散，所以要把所有 2 一起放进队列。

~~~text
初始 t = 0：
2 1 1
1 1 0
0 1 1

t = 1：
2 2 1
2 1 0
0 1 1

t = 2：
2 2 2
2 2 0
0 1 1

t = 3：
2 2 2
2 2 0
0 2 1

t = 4：
2 2 2
2 2 0
0 2 2
~~~

每一层队列代表同一分钟发生的腐烂：

~~~mermaid
flowchart LR
    A["所有初始 2"] --> B["第 0 分钟队列"]
    B --> C["扩散到相邻 1"]
    C --> D["第 1 分钟队列"]
    D --> E["继续按层扩散"]
    E --> F["没有 1：返回分钟数"]
~~~

<iframe
  src="http://127.0.0.1:8765/notes/algorithms/graphs/oranges.html"
  width="100%"
  height="650"
  title="994 腐烂的橘子多源 BFS 动画"
  loading="eager"
  style="border:0; border-radius:16px;">
</iframe>

### 3. Java 标准写法

~~~java
class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;
        Queue<int[]> queue = new ArrayDeque<>();
        int fresh = 0;

        // 先把所有腐烂橘子放进队列，同时统计新鲜橘子
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int minutes = 0;

        while (!queue.isEmpty() && fresh > 0) {
            // 当前这一层的橘子，代表同一分钟开始扩散
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int[] orange = queue.poll();
                int r = orange[0];
                int c = orange[1];

                // 下
                if (r + 1 < m && grid[r + 1][c] == 1) {
                    grid[r + 1][c] = 2;
                    fresh--;
                    queue.offer(new int[]{r + 1, c});
                }

                // 上
                if (r - 1 >= 0 && grid[r - 1][c] == 1) {
                    grid[r - 1][c] = 2;
                    fresh--;
                    queue.offer(new int[]{r - 1, c});
                }

                // 右
                if (c + 1 < n && grid[r][c + 1] == 1) {
                    grid[r][c + 1] = 2;
                    fresh--;
                    queue.offer(new int[]{r, c + 1});
                }

                // 左
                if (c - 1 >= 0 && grid[r][c - 1] == 1) {
                    grid[r][c - 1] = 2;
                    fresh--;
                    queue.offer(new int[]{r, c - 1});
                }
            }

            minutes++;
        }

        return fresh == 0 ? minutes : -1;
    }
}
~~~

### 4. queue.size() 的作用

~~~text
队列开始：[本分钟的腐烂橘子 A，本分钟的腐烂橘子 B]

先记住 size = 2，只处理 A 和 B。
它们新感染的橘子虽然加入队列，但属于下一分钟。

处理 A、B 后：
队列 = [下一分钟的新橘子们]
minutes 加一
下一轮再处理这些新橘子
~~~

如果不保存 size，而是直接把当前队列一直处理到空，就会把多个分钟压缩成一次，答案会偏小。

### 5. 复杂度与易错点

- 时间 O(m × n)；
- 队列空间最坏 O(m × n)；
- 不能只从第一个腐烂橘子开始，必须所有 2 同时入队；
- 新鲜橘子变成 2 时立刻 fresh--；
- 最后 fresh > 0 说明存在无法到达的新鲜橘子，返回 -1；
- minutes 应该在处理一整层之后加一。

---

## 四、207. 课程表

### 1. 把题目翻译成图

prerequisites[i] = [a, b] 表示：

> 想学习课程 a，必须先学习课程 b。

所以图中应该画成：

~~~text
[a, b]：b  ——→  a
       先修    后修
~~~

例如：

~~~text
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

      0
     / \
    1   2
     \ /
      3
~~~

~~~mermaid
flowchart TD
    C0["课程 0"] --> C1["课程 1"]
    C0 --> C2["课程 2"]
    C1 --> C3["课程 3"]
    C2 --> C3
~~~

<iframe
  src="http://127.0.0.1:8765/notes/algorithms/graphs/course-schedule.html"
  width="100%"
  height="650"
  title="207 课程表拓扑排序动画"
  loading="eager"
  style="border:0; border-radius:16px;">
</iframe>

### 2. 核心判断：有向图有没有环

~~~text
无环：
0 ——→ 1 ——→ 2

有环：
0 ——→ 1 ——→ 2
↑             │
└─────────────┘
~~~

如果出现环：

~~~text
0 要等 2
2 要等 1
1 又要等 0

谁都没有办法先开始，课程无法全部完成。
~~~

因此本题等价于：判断有向图是否有环。

### 3. 方法一：Kahn 算法（BFS 拓扑排序）

一个节点的入度，就是指向它的边数量。

~~~text
0 ——→ 1 ——→ 3
└——→ 2 ——→ 3

indegree[0] = 0
indegree[1] = 1
indegree[2] = 1
indegree[3] = 2
~~~

入度为 0 的课程不需要等待任何先修课，可以直接学习。每学完一门课，就让它的后继课程入度减一；减成 0 就加入队列。

~~~mermaid
flowchart LR
    A["找入度为 0 的课程"] --> B["加入队列"]
    B --> C["学完并出队"]
    C --> D["后继课程入度 - 1"]
    D --> E{"入度是否为 0"}
    E -- 是 --> B
    E -- 否 --> C
    C --> F["统计已完成课程数"]
~~~

#### Java 代码

~~~java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }

        int[] indegree = new int[numCourses];

        for (int[] pair : prerequisites) {
            int course = pair[0];
            int prerequisite = pair[1];

            // prerequisite -> course
            graph[prerequisite].add(course);
            indegree[course]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int finished = 0;

        while (!queue.isEmpty()) {
            int currentCourse = queue.poll();
            finished++;

            for (int nextCourse : graph[currentCourse]) {
                indegree[nextCourse]--;
                if (indegree[nextCourse] == 0) {
                    queue.offer(nextCourse);
                }
            }
        }

        return finished == numCourses;
    }
}
~~~

记忆方式：

~~~text
入度 0：现在能学
出队：学完这门课
邻居入度减一：释放后继课程
最后数量不够：图中有环
~~~

### 4. 方法二：DFS 三色标记

| 状态 | 含义 |
| --- | --- |
| 0 | 没访问过 |
| 1 | 当前 DFS 路径中，正在访问 |
| 2 | 已经访问完成 |

如果 DFS 过程中再次遇到状态 1 的节点，说明沿着当前路径走回来了，存在环。

~~~text
访问 0：color[0] = 1
访问 1：color[1] = 1
访问 2：color[2] = 1

如果 2 又指向 0：
遇到 color[0] == 1
=> 当前路径成环
~~~

~~~java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] pair : prerequisites) {
            int course = pair[0];
            int prerequisite = pair[1];
            graph[prerequisite].add(course);
        }

        int[] color = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (color[i] == 0 && hasCycle(graph, color, i)) {
                return false;
            }
        }

        return true;
    }

    private boolean hasCycle(List<Integer>[] graph, int[] color, int node) {
        if (color[node] == 1) {
            return true;
        }
        if (color[node] == 2) {
            return false;
        }

        color[node] = 1;

        for (int nextCourse : graph[node]) {
            if (hasCycle(graph, color, nextCourse)) {
                return true;
            }
        }

        color[node] = 2;
        return false;
    }
}
~~~

### 5. 复杂度与易错点

- 时间 O(V + E)；
- 邻接表和辅助数组 O(V + E)；
- [a, b] 是 b -> a，不要把边方向写反；
- DFS 中 1 是当前路径，2 是已经完成；
- Kahn 最后判断 finished == numCourses，不是队列是否为空。

---

## 五、208. 实现 Trie（前缀树）

### 1. Trie 是什么

Trie 把字符串拆成一个个字符，让拥有相同前缀的单词共享路径。

插入 cat、car、dog 后：

~~~text
root
├── c
│   └── a
│       ├── t  （完整单词 cat）
│       └── r  （完整单词 car）
└── d
    └── o
        └── g  （完整单词 dog）
~~~

节点表示“走到这里有一个前缀”，isWord 才表示“走到这里刚好有一个完整单词”。

~~~mermaid
flowchart TD
    R(("root")) --> C["c"]
    C --> A["a"]
    A --> T["t ●"]
    A --> CAR["r ●"]
    R --> D["d"]
    D --> O["o"]
    O --> G["g ●"]
~~~

<iframe
  src="http://127.0.0.1:8765/notes/algorithms/graphs/trie.html"
  width="100%"
  height="650"
  title="208 Trie 前缀树动画"
  loading="eager"
  style="border:0; border-radius:16px;">
</iframe>

图中的 ● 表示 isWord = true。

### 2. 节点结构

如果题目只包含小写英文字母，可以用长度为 26 的数组：

~~~java
Node[] children = new Node[26];
~~~

字符到下标的转换：

~~~java
int index = c - 'a';
~~~

例如：

~~~text
'a' - 'a' = 0
'c' - 'a' = 2
'z' - 'a' = 25
~~~

### 3. Java 完整实现

~~~java
class Trie {
    private static class Node {
        Node[] children = new Node[26];
        boolean isWord;
    }

    private final Node root = new Node();

    public Trie() {
    }

    public void insert(String word) {
        Node current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a';

            // 没有这条字符边，就创建一个新节点
            if (current.children[index] == null) {
                current.children[index] = new Node();
            }

            // 沿着当前字符走到下一个节点
            current = current.children[index];
        }

        // 能走到单词末尾，才标记为完整单词
        current.isWord = true;
    }

    public boolean search(String word) {
        Node node = findNode(word);
        if (node == null) {
            return false;
        }
        return node.isWord;
    }

    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }

    private Node findNode(String text) {
        Node current = root;

        for (char c : text.toCharArray()) {
            int index = c - 'a';

            if (current.children[index] == null) {
                return null;
            }

            current = current.children[index];
        }

        return current;
    }
}
~~~

### 4. search 和 startsWith 的区别

假设 Trie 中只插入了 apple：

~~~text
search("app")        false
startsWith("app")    true

search("apple")      true
startsWith("apple")  true
~~~

findNode("app") 能走到节点，说明它是前缀；但 app 节点的 isWord 是 false，说明它不是完整单词。

### 5. 如果字符不只包含小写字母

题目限定小写字母时，数组最快、代码最简单。如果字符范围很大，可以把节点改成：

~~~java
Map<Character, Node> children = new HashMap<>();
~~~

对应操作：

~~~java
current.children.putIfAbsent(c, new Node());
current = current.children.get(c);
~~~

代价是代码稍复杂、常数更大，但可以支持更多字符。

### 6. 复杂度

设字符串长度为 L：

- insert：O(L)；
- search：O(L)；
- startsWith：O(L)；
- 数组版每个节点额外占用 26 个引用空间。

---

## 六、四道题的统一对比

| 题目 | “节点”是什么 | “边”是什么 | 访问标记 | 答案如何产生 |
| --- | --- | --- | --- | --- |
| 岛屿数量 | 一个网格格子 | 上下左右相邻 | 1 -> 0 或 visited | 发现新陆地时 count++ |
| 腐烂的橘子 | 一个网格格子 | 上下左右扩散 | 1 -> 2 | BFS 层数就是分钟 |
| 课程表 | 一门课程 | 先修课指向后修课 | 入度 / 三色状态 | 能否处理完所有节点 |
| Trie | 一个前缀节点 | 下一个字符 | 是否存在子节点 | 路径存在，且末尾 isWord |

~~~mermaid
mindmap
  root((图论与 Trie))
    网格
      岛屿数量
        连通块
        DFS/BFS
        标记访问
      腐烂的橘子
        多源 BFS
        分层计时
    有向图
      课程表
        拓扑排序
        入度
        环检测
    前缀树
      字符路径
      isWord
      search
      startsWith
~~~

---

## 七、最后的解题模板

### 网格 DFS 模板

~~~java
void dfs(int[][] grid, int r, int c) {
    if (越界 || 当前状态不是目标状态) {
        return;
    }

    标记当前状态;

    for (四个方向) {
        dfs(grid, nr, nc);
    }
}
~~~

### 多源 BFS 模板

~~~java
把所有初始源点一起加入 queue;

while (!queue.isEmpty()) {
    int size = queue.size(); // 当前层

    for (int i = 0; i < size; i++) {
        取出当前点;
        扩展相邻点;
        把新状态加入下一层;
    }

    distance++;
}
~~~

### 拓扑排序模板

~~~java
建立 graph 和 indegree;
把所有 indegree == 0 的点加入 queue;

while (!queue.isEmpty()) {
    int node = queue.poll();
    统计 node 已处理;

    for (int next : graph[node]) {
        if (--indegree[next] == 0) {
            queue.offer(next);
        }
    }
}

处理数量 == 节点总数：无环
处理数量 <  节点总数：有环
~~~

### Trie 模板

~~~java
Node current = root;

for (char c : text.toCharArray()) {
    int index = c - 'a';
    if (current.children[index] == null) {
        current.children[index] = new Node();
    }
    current = current.children[index];
}
~~~

### 最终记忆口诀

> 岛屿：发现 1，数一个，搜到的 1 全部淹掉。  
> 橘子：所有 2 一起入队，一层就是一分钟。  
> 课程：先修课指向后修课，入度为零才能出队。  
> Trie：字符一层一层走，末尾标记才是完整单词。
