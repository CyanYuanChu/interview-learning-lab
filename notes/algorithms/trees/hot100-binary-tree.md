# Hot 100 二叉树：统一解题框架与题型模板

这份笔记整理 Hot 100 中常见的二叉树题目，重点不是背每道题的代码，而是掌握一套可以反复套用的思考方式。

覆盖题目：

- 94 二叉树的中序遍历
- 104 二叉树的最大深度
- 226 翻转二叉树
- 101 对称二叉树
- 543 二叉树的直径
- 102 二叉树的层序遍历
- 108 将有序数组转换为二叉搜索树
- 98 验证二叉搜索树
- 230 二叉搜索树中第 K 小的元素
- 199 二叉树的右视图
- 114 二叉树展开为链表
- 105 从前序与中序遍历序列构造二叉树
- 437 路径总和 III
- 236 二叉树的最近公共祖先
- 124 二叉树中的最大路径和

---

## 一、二叉树题目的共同本质

最重要的一句话是：

> 每个节点都是一棵更小的二叉树。先解决左子树和右子树，再在当前节点合并结果。

大多数递归题都可以抽象为：

```text
dfs(node)
    ├── node 为空？返回基础值
    ├── left  = dfs(node.left)
    ├── right = dfs(node.right)
    ├── 利用 left、right 和 node.val 处理当前节点
    └── 返回父节点需要的信息
```

真正需要思考的不是“怎么遍历”，而是：

> dfs(root) 到底代表什么？

例如：

```text
dfs(root) 返回 root 子树的高度
dfs(root) 返回 root 向下延伸的最大路径和
dfs(root) 返回 root 子树的最小值和最大值
dfs(root) 返回 root 子树中找到的目标节点
```

只要这句话定义清楚，代码通常就是把这句话翻译出来。

---

## 二、通用递归模板

### 1. 一个返回值：子树信息型

适合最大深度、直径、最大路径和等题目。

```java
class Solution {
    private int answer;

    public int solve(TreeNode root) {
        answer = 0;
        dfs(root);
        return answer;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = dfs(root.left);
        int right = dfs(root.right);

        // 利用 left、right 和 root.val 处理当前节点

        // 返回父节点需要的信息
        return 0;
    }
}
```

### 2. 多个返回值：封装一个结果类

Java 没有 C++ 的 tuple，可以自己定义 Info：

```java
private static class Info {
    long min;
    long max;

    Info(long min, long max) {
        this.min = min;
        this.max = max;
    }
}
```

使用方式：

```java
Info left = dfs(root.left);
Info right = dfs(root.right);
```

### 3. 向下传递状态型

父节点把信息传给子节点，适合验证 BST、记录路径、记录深度等问题。

```java
private void dfs(TreeNode root, long low, long high) {
    if (root == null) {
        return;
    }

    // 当前节点必须满足 low < root.val < high

    dfs(root.left, low, root.val);
    dfs(root.right, root.val, high);
}
```

### 4. 全局答案型

有些信息不能完整地通过返回值传给父节点，需要额外记录答案：

```java
private int answer;

public int solve(TreeNode root) {
    answer = Integer.MIN_VALUE;
    dfs(root);
    return answer;
}
```

典型题目：

- 543 二叉树的直径
- 124 二叉树中的最大路径和
- 437 路径总和 III

---

## 三、到底选择哪种遍历？

### 前序遍历：根 → 左 → 右

先处理当前节点，再把状态传给孩子。

适合：

- 根到叶路径
- 向下传递上下界
- 记录深度
- 构造或修改树

### 中序遍历：左 → 根 → 右

BST 的中序遍历天然升序。

适合：

- BST 第 K 小元素
- 验证 BST 的严格递增性
- 输出有序节点序列

### 后序遍历：左 → 右 → 根

必须先拿到左右子树的信息，再处理当前节点。

适合：

- 最大深度
- 直径
- 最大路径和
- 判断平衡
- 统计子树信息

### BFS：一层一层处理

适合：

- 层序遍历
- 右视图
- 最短层数
- 按层统计节点

一个简单的选择标准：

```text
需要孩子的结果：后序 DFS
需要父节点传状态：前序 DFS
需要层信息：BFS
BST 需要有序顺序：中序 DFS
比较两棵镜像树：双节点 DFS
```

---

## 四、最重要的区别：返回值和全局答案

### 例子：最大路径和

在节点 20：

```text
左边返回 15，右边返回 7
经过当前节点的完整路径：15 + 20 + 7 = 42
```

所以更新全局答案：

```java
answer = Math.max(answer, left + root.val + right);
```

但是返回父节点时，路径不能分叉，只能选择左边或右边的一条：

```java
return root.val + Math.max(left, right);
```

因此要记住：

> dfs 返回单边，answer 记录双边拐点。

这条规律同时贯穿：

- 543 二叉树的直径
- 124 二叉树中的最大路径和

---

## 五、Hot 100 二叉树题目总览

| 题目 | 主要遍历 | dfs 或队列的核心含义 | 关键模板 |
|---|---|---|---|
| 94 中序遍历 | 中序 | 左、根、右 | 递归或栈 |
| 104 最大深度 | 后序 | 返回子树高度 | 1 + max(left,right) |
| 226 翻转二叉树 | 前序/后序 | 修改左右指针 | 交换 left/right |
| 101 对称二叉树 | 双节点 DFS | 比较两棵镜像子树 | 外侧对外侧、内侧对内侧 |
| 543 二叉树直径 | 后序 | 返回单侧高度 | 全局记录左右高度之和 |
| 102 层序遍历 | BFS | 当前层节点数量 | 固定 size |
| 108 有序数组转 BST | 分治 | 当前区间构造子树 | 中点作为根 |
| 98 验证 BST | DFS/中序 | 合法范围或递增序列 | 不能只看父子节点 |
| 230 BST 第 K 小 | 中序 | 第 K 次访问的节点 | count-- |
| 199 右视图 | BFS/右优先 DFS | 每层最右节点 | 每层最后或第一次 |
| 114 展开为链表 | 前序/反向前序 | 维护前驱节点 | 所有节点接到 right |
| 105 构造二叉树 | 分治 | 前序找根，中序分区 | 哈希表定位根 |
| 437 路径总和 III | DFS + 前缀和 | 根到当前的前缀和 | 查 sum-target，回溯撤销 |
| 236 最近公共祖先 | 后序 | 子树中找到的节点 | 左右都找到就返回当前 |
| 124 最大路径和 | 后序 | 向上延伸的最大单边和 | 全局记录完整路径 |

---

## 六、各题如何套用统一思想

### 94. 二叉树的中序遍历

递归模板：

```java
private void inorder(TreeNode root, List<Integer> result) {
    if (root == null) {
        return;
    }

    inorder(root.left, result);
    result.add(root.val);
    inorder(root.right, result);
}
```

核心：

```text
中序 = 左 → 根 → 右
```

这道题是遍历基础，也是 BST 题目的基础。

---

### 104. 二叉树的最大深度

定义：

```text
dfs(root) 返回 root 子树的最大高度
```

```java
private int dfs(TreeNode root) {
    if (root == null) {
        return 0;
    }

    int left = dfs(root.left);
    int right = dfs(root.right);

    return Math.max(left, right) + 1;
}
```

核心公式：

```text
当前高度 = max(左高度, 右高度) + 1
```

---

### 226. 翻转二叉树

当前节点要做的事情只有一个：交换左右孩子。

```java
public TreeNode invertTree(TreeNode root) {
    if (root == null) {
        return null;
    }

    TreeNode temp = root.left;
    root.left = root.right;
    root.right = temp;

    invertTree(root.left);
    invertTree(root.right);

    return root;
}
```

核心：

```text
修改当前节点，再递归处理子树。
```

交换之后递归的是新的 root.left 和 root.right。

---

### 101. 对称二叉树

这题不是比较一个节点，而是比较两个节点：

```text
left 和 right 是否互为镜像？
```

```java
private boolean isMirror(TreeNode left, TreeNode right) {
    if (left == null || right == null) {
        return left == right;
    }

    if (left.val != right.val) {
        return false;
    }

    return isMirror(left.left, right.right)
            && isMirror(left.right, right.left);
}
```

核心对应关系：

```text
左树的左边 ↔ 右树的右边
左树的右边 ↔ 右树的左边
```

left == right 的含义：

- 两个都是 null：对称
- 一个是 null：不对称

---

### 543. 二叉树的直径

定义：

```text
dfs(root) 返回从 root 向下延伸的最大高度
```

```java
class Solution {
    private int answer = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return answer;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = dfs(root.left);
        int right = dfs(root.right);

        // 经过当前节点的直径，按边数计算
        answer = Math.max(answer, left + right);

        // 返回给父节点的只能是一条向下的路径
        return Math.max(left, right) + 1;
    }
}
```

关键区别：

```text
更新答案：left + right
返回父节点：max(left, right) + 1
```

直径按边数计算，所以叶子的高度是 0。

---

### 102. 二叉树的层序遍历

BFS 模板：

```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) {
        return result;
    }

    Deque<TreeNode> queue = new ArrayDeque<>();
    queue.offer(root);

    while (!queue.isEmpty()) {
        int size = queue.size();
        List<Integer> level = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);

            if (node.left != null) {
                queue.offer(node.left);
            }
            if (node.right != null) {
                queue.offer(node.right);
            }
        }

        result.add(level);
    }

    return result;
}
```

最重要的一句：

```java
int size = queue.size();
```

它把当前层和下一层分开。当前层遍历时，新加入队列的节点属于下一层，不能在这一轮处理。

---

### 108. 将有序数组转换为平衡 BST

定义：

```text
用 nums[left...right] 构造一棵平衡 BST
```

```java
private TreeNode build(int[] nums, int left, int right) {
    if (left > right) {
        return null;
    }

    int mid = left + (right - left) / 2;
    TreeNode root = new TreeNode(nums[mid]);

    root.left = build(nums, left, mid - 1);
    root.right = build(nums, mid + 1, right);

    return root;
}
```

核心：

```text
中点作为根，左区间构造左子树，右区间构造右子树。
```

---

### 98. 验证二叉搜索树

只比较父子节点是不够的。例如左子树中更深的位置出现一个大于根节点的值，仍然是非法 BST。

更推荐使用上下界：

```java
public boolean isValidBST(TreeNode root) {
    return check(root, Long.MIN_VALUE, Long.MAX_VALUE);
}

private boolean check(TreeNode root, long low, long high) {
    if (root == null) {
        return true;
    }

    if (root.val <= low || root.val >= high) {
        return false;
    }

    return check(root.left, low, root.val)
            && check(root.right, root.val, high);
}
```

核心：

```text
左子树必须处于 (low, root.val)
右子树必须处于 (root.val, high)
```

BST 通常要求严格不等，因此重复值也不合法。

---

### 230. BST 中第 K 小的元素

BST 中序遍历是升序，所以第 k 次访问到的节点就是答案。

```java
class Solution {
    private int count;
    private int result;

    public int kthSmallest(TreeNode root, int k) {
        count = k;
        dfs(root);
        return result;
    }

    private void dfs(TreeNode root) {
        if (root == null || count == 0) {
            return;
        }

        dfs(root.left);

        if (count == 0) {
            return;
        }

        --count;
        if (count == 0) {
            result = root.val;
            return;
        }

        dfs(root.right);
    }
}
```

核心顺序：

```text
左子树 → count-- → 当前节点 → 右子树
```

Java 中 int 是值传递，所以不能指望递归参数中的 k 自动改变外层变量。这里使用成员变量 count。

---

### 199. 二叉树的右视图

方法一：BFS，每层最后一个节点就是右视图节点。

```java
for (int i = 0; i < size; i++) {
    TreeNode node = queue.poll();

    if (i == size - 1) {
        result.add(node.val);
    }
}
```

方法二：右优先 DFS：

```java
private void dfs(TreeNode root, int depth, List<Integer> result) {
    if (root == null) {
        return;
    }

    if (depth == result.size()) {
        result.add(root.val);
    }

    dfs(root.right, depth + 1, result);
    dfs(root.left, depth + 1, result);
}
```

右优先 DFS 的逻辑是：

```text
每层第一次遇到的节点，就是最右侧节点。
```

---

### 114. 二叉树展开为链表

目标结构：

```text
所有节点按照前序顺序排列
所有 left 都为 null
所有节点通过 right 连接
```

一种直观做法：

```java
public void flatten(TreeNode root) {
    if (root == null) {
        return;
    }

    flatten(root.left);
    flatten(root.right);

    TreeNode oldRight = root.right;

    root.right = root.left;
    root.left = null;

    TreeNode tail = root;
    while (tail.right != null) {
        tail = tail.right;
    }

    tail.right = oldRight;
}
```

覆盖 root.right 前必须先保存原来的右子树。

---

### 105. 从前序与中序遍历构造二叉树

前序遍历的第一个节点一定是根节点。中序遍历中，根左边是左子树，根右边是右子树。

```java
class Solution {
    private int preorderIndex;
    private Map<Integer, Integer> inorderIndex = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            inorderIndex.put(inorder[i], i);
        }

        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int left, int right) {
        if (left > right) {
            return null;
        }

        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);

        int mid = inorderIndex.get(rootValue);
        root.left = build(preorder, left, mid - 1);
        root.right = build(preorder, mid + 1, right);

        return root;
    }
}
```

核心：

```text
前序找根，中序切左右，递归构造。
```

---

### 437. 路径总和 III

这题的路径不一定从根开始，但必须从上到下。

假设当前前缀和是 currentSum，如果之前出现过：

```text
currentSum - targetSum
```

就说明中间有一条路径的和等于 targetSum。

```java
class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> prefix = new HashMap<>();
        prefix.put(0L, 1);
        return dfs(root, targetSum, 0L, prefix);
    }

    private int dfs(TreeNode root,
                     int targetSum,
                     long currentSum,
                     Map<Long, Integer> prefix) {
        if (root == null) {
            return 0;
        }

        currentSum += root.val;

        int result = prefix.getOrDefault(
                currentSum - targetSum, 0);

        prefix.put(currentSum,
                prefix.getOrDefault(currentSum, 0) + 1);

        result += dfs(root.left, targetSum, currentSum, prefix);
        result += dfs(root.right, targetSum, currentSum, prefix);

        // 回溯：不能污染兄弟子树
        prefix.put(currentSum, prefix.get(currentSum) - 1);

        return result;
    }
}
```

最重要的不是普通递归，而是：

```text
进入节点：加入前缀和
离开节点：撤销前缀和
```

---

### 236. 二叉树的最近公共祖先

定义 dfs(root)：

```text
返回当前子树中找到的 p 或 q 节点；都没找到就返回 null。
```

```java
public TreeNode lowestCommonAncestor(TreeNode root,
                                     TreeNode p,
                                     TreeNode q) {
    if (root == null || root == p || root == q) {
        return root;
    }

    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);

    if (left != null && right != null) {
        return root;
    }

    return left != null ? left : right;
}
```

判断逻辑：

```text
当前节点是 p/q：返回当前节点
左边找到、右边也找到：当前节点是 LCA
只有一边找到：返回那一边
两边都没找到：返回 null
```

---

### 124. 二叉树中的最大路径和

定义：

```text
dfs(root) 返回从 root 出发、向下延伸的一条最大路径和。
```

```java
class Solution {
    private int answer = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        answer = Integer.MIN_VALUE;
        dfs(root);
        return answer;
    }

    private int dfs(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = Math.max(0, dfs(root.left));
        int right = Math.max(0, dfs(root.right));

        // 当前节点作为拐点，可以同时连接左右两边
        answer = Math.max(answer, left + root.val + right);

        // 返回父节点时只能选择一边
        return root.val + Math.max(left, right);
    }
}
```

为什么要和 0 比较？

```text
如果某个子树贡献为负数，不如不走这条子树。
```

为什么 answer 初始化为 Integer.MIN_VALUE？

```text
因为整棵树可能全部是负数，不能初始化为 0。
```

---

## 七、几个模板如何互相贯穿

### 模板 A：后序返回高度

同时出现在：

- 104 最大深度
- 543 二叉树直径
- 平衡二叉树

共同点：

```java
int left = dfs(root.left);
int right = dfs(root.right);
return Math.max(left, right) + 1;
```

区别只是当前节点如何利用 left 和 right：

```text
最大深度：返回高度
直径：用左右高度更新全局答案
平衡：检查左右高度差
```

### 模板 B：后序返回单边贡献

同时出现在：

- 543 二叉树直径
- 124 最大路径和

共同点：

```text
左右两边可以在当前节点汇合，形成完整答案；
但返回父节点时只能选择一边。
```

### 模板 C：BST 中序有序

同时出现在：

- 94 中序遍历
- 98 验证 BST
- 230 BST 第 K 小

共同点：

```text
BST 的中序遍历结果是严格递增序列。
```

因此：

```text
输出序列：直接中序
验证合法性：检查是否递增
第 K 小：中序访问第 K 个
```

### 模板 D：层级信息

同时出现在：

- 102 层序遍历
- 199 右视图

共同点：

```java
int size = queue.size();
```

先固定当前层节点数量，再处理这一层。

### 模板 E：全局状态和回溯

同时出现在：

- 437 路径总和 III
- 124 最大路径和
- 543 二叉树直径

共同点：

```text
递归返回局部信息；成员变量或哈希表记录全局状态。
```

如果状态只对当前分支有效，离开节点时必须撤销，这就是回溯。

---

## 八、Java 与 C++ 的常用转换

| C++ | Java | 含义 |
|---|---|---|
| root->val | root.val | 访问节点值 |
| root->left | root.left | 访问左子树 |
| nullptr | null | 空指针 |
| vector<int> | List<Integer> | 动态数组 |
| unordered_map | HashMap | 哈希表 |
| queue<TreeNode*> | Deque<TreeNode> | 队列 |
| stack<TreeNode*> | Deque<TreeNode> | 栈 |
| max(a,b) | Math.max(a,b) | 两数取最大值 |
| tuple | 自定义 Info/Result 类 | 多个返回值 |
| int& k | 成员变量或 int[] | 共享可修改状态 |
| LONG_MAX | Long.MAX_VALUE | long 最大值 |
| INT_MIN | Integer.MIN_VALUE | int 最小值 |

Java 的 Math.max 一次只能比较两个值：

```java
Math.max(Math.max(a, b), c);
```

---

## 九、最容易犯的错误

### 1. 没有先定义 dfs 的含义

错误思路：

```text
我先把左右递归写出来再说。
```

正确思路：

```text
dfs(root) 返回什么？是高度、路径和、节点、范围，还是布尔值？
```

### 2. 只检查 BST 的父子关系

BST 要满足整棵子树的范围，不只是：

```text
左孩子 < 父节点 < 右孩子
```

应该使用上下界或中序递增判断。

### 3. 把完整路径返回给父节点

路径一旦向上延伸，就只能选择左边或右边一条，不能同时带两边，否则路径会分叉。

### 4. 全局答案没有初始化为负无穷

最大路径和可能全部是负数，不能把答案初始化为 0。

### 5. BFS 没有固定当前层大小

正确写法：

```java
int size = queue.size();
```

### 6. 路径总和没有回溯

兄弟子树不能使用另一条分支留下的前缀和：

```java
prefix.put(currentSum, prefix.get(currentSum) - 1);
```

### 7. Java 的 int 参数不会被递归共享修改

```java
void dfs(TreeNode root, int k)
```

递归中修改 k 不会改变调用者的基本类型变量。需要使用成员变量、int[] 或自定义可变对象。

---

## 十、做题时固定问自己的六个问题

1. 这道题需要前序、中序、后序，还是 BFS？
2. dfs(root) 的一句话定义是什么？
3. root == null 时返回什么？
4. 左右子树返回的信息如何合并？
5. 返回给父节点的内容是什么？
6. 最终答案是否需要额外的全局变量或哈希表？

可以把解题过程写成下面这样：

```text
定义：dfs(root) 表示……
空节点：返回……
左子树：得到 left……
右子树：得到 right……
当前节点：用 left、right、root.val 计算……
返回：父节点只需要……
全局答案：在当前节点更新……
```

---

## 十一、最后的总口诀

```text
树题先想子树，
递归先定返回值；
孩子信息用后序，
父传状态用前序；
BST 中序天然有序，
层级问题优先 BFS；
路径向上只能单边，
完整答案用全局记录；
进入分支记录状态，
离开分支记得回溯。
```

真正掌握二叉树，不是背十五份代码，而是能够对每道题说清楚：

> 当前节点从左右子树拿到什么信息？它如何合并？又应该把什么信息交给父节点？
