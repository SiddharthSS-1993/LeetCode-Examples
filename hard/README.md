# Hard Level Problems

This section contains documented solutions to LeetCode Hard problems.

Each entry includes: **problem link, question, intuition, approach, and complexity.**

---
<details><summary>Tree</summary>

### 0124. Binary Tree Maximum Path Sum  
🔗 https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

**Question**
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes is connected by an edge.

A path does not need to pass through the root. The path sum is the sum of the values of the nodes in the path.

Return the maximum path sum of any path in the tree.

**Intuition**
Why DFS?

Every node needs information from its left and right subtrees.
DFS naturally solves the smaller subtrees first and then combines their answers to compute the result for the current node.

Unlike Maximum Depth from problem 0104, this problem requires two values:

1. Current Path
   node.val + left_gain + right_gain
   Used to update the global answer.

2. Return Value
   node.val + max(left_gain, right_gain)

   Returned to the parent because a path can continue through
   only one child.

**Approach**
1. Use Depth First Search (DFS) to traverse the tree.
2. For every node, recursively calculate the maximum   contribution from the left and right subtrees.
3. Ignore negative contributions because they decrease the path sum.
4. Calculate the maximum path passing through the current node:
   node.val + left_gain + right_gain
5. Update the global maximum path sum.
6. Return only one branch to the parent:
   node.val + max(left_gain, right_gain)

A parent cannot continue through both branches because a path
cannot split into two directions.

**Dry Run**

        -10
        /  \
       9    20
           /  \
          15   7

Initially start traversing left from Node 10
Node 9

left_gain = 0
right_gain = 0

current_path = 9

maximum_sum = 9
return = 9 + max(0,0) = 9

--------------------------
Traverse back to right of root 10 and then right of 10, 20 and then to the left of 20, 15
Node 15

left_gain = 0
right_gain = 0

current_path = 15
maximum_sum = 15
return = 15 + max(0, 0) = 15

--------------------------
Traverse back to 20 and look into the right of 20, 7
Node 7

left_gain = 0
right_gain = 0

current_path = 7
maximum_sum = 7
return = 7 + max(0,0) = 7

--------------------------
Now that we have max_path for 15 and 7 traverse to 20
Node 20

left_gain = 15
right_gain = 7

current_path = 20 + 15 + 7 = 42

maximum_sum = 42

return = 20 + max(15,7) = 35

--------------------------
Traverse back to root node -10
Node -10
left_gain = 9
right_gain = 35

current_path = -10 + 9 + 35 = 34
maximum_sum remains 42
return = -10 + max(9,35) = 25

Final Answer = 42

--------------------------

**Time Complexity**
O(n)
Every node is visited exactly once(Although we said traverse back to different nodes. it is handled through recursion).

Space Complexity
O(h)
h is the height of the tree.
Worst case: O(n)
Balanced tree: O(log n)
