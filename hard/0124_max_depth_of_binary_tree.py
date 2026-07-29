# Question
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes is connected by an edge.
#
# A path does not need to pass through the root.
#
# The path sum is the sum of the values of the nodes in the path.
#
# Return the maximum path sum of any path in the tree.

# Approach
# 1. Use Depth First Search (DFS) to traverse the tree.
# 2. For every node, recursively calculate the maximum contribution
#    from the left and right subtrees.
# 3. Ignore negative contributions because they decrease the path sum.
# 4. Calculate the maximum path passing through the current node:
#
#       node.val + left_gain + right_gain
#
# 5. Update the global maximum path sum.
# 6. Return only one branch to the parent:
#
#       node.val + max(left_gain, right_gain)
#
#    A parent cannot continue through both branches because a path
#    cannot split into two directions.

# Why DFS?
#
# Every node needs information from its left and right subtrees.
#
# DFS naturally solves the smaller subtrees first and then combines
# their answers to compute the result for the current node.
#
# Unlike Maximum Depth, this problem requires two values:
#
# 1. Current Path
#    node.val + left_gain + right_gain
#
#    Used to update the global answer.
#
# 2. Return Value
#    node.val + max(left_gain, right_gain)
#
#    Returned to the parent because a path can continue through
#    only one child.

# Dry Run
#
#         -10
#         /  \
#        9    20
#            /  \
#           15   7
#
# Node 9
#
# left_gain = 0
# right_gain = 0
#
# current_path = 9
#
# maximum_sum = 9
#
# return = 9
#
# --------------------------
#
# Node 15
#
# left_gain = 0
# right_gain = 0
#
# current_path = 15
#
# maximum_sum = 15
#
# return = 15
#
# --------------------------
#
# Node 7
#
# left_gain = 0
# right_gain = 0
#
# current_path = 7
#
# maximum_sum = 15
#
# return = 7
#
# --------------------------
#
# Node 20
#
# left_gain = 15
# right_gain = 7
#
# current_path = 20 + 15 + 7 = 42
#
# maximum_sum = 42
#
# return = 20 + max(15,7)
#
# = 35
#
# --------------------------
#
# Node -10
#
# left_gain = 9
# right_gain = 35
#
# current_path = -10 + 9 + 35 = 34
#
# maximum_sum remains 42
#
# return = -10 + max(9,35)
#
# = 25
#
# Final Answer = 42

# Time Complexity
# O(n)
#
# Every node is visited exactly once.

# Space Complexity
# O(h)
#
# h is the height of the tree.
#
# Worst case: O(n)
# Balanced tree: O(log n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maximum_sum = float("-inf")

        def dfs(node):
            # An empty child contributes nothing.
            if node is None:
                return 0

            # Ignore a subtree if its best contribution is negative.
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Best complete path passing through this node.
            current_path_sum = node.val + left_gain + right_gain

            # Update the best path found anywhere in the tree.
            self.maximum_sum = max(
                self.maximum_sum,
                current_path_sum
            )

            # A parent can continue through only one branch.
            return node.val + max(left_gain, right_gain)

        dfs(root)

        return self.maximum_sum
        