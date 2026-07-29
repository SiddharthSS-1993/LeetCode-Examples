# Question
# Given the root of a binary tree, invert the tree and return its root.
#
# Inverting a binary tree means swapping the left and right child
# of every node.
#
# Example:
#
# Original:
#
#         4
#       /   \
#      2     7
#     / \   / \
#    1   3 6   9
#
# Inverted:
#
#         4
#       /   \
#      7     2
#     / \   / \
#    9   6 3   1

# Approach
# 1. If the current node is None, return None.
# 2. Recursively invert the left subtree.
# 3. Recursively invert the right subtree.
# 4. Swap the two returned subtrees.
# 5. Return the current root.

# Why DFS?
#
# Every node performs the same task:
#
# 1. Invert its left subtree.
# 2. Invert its right subtree.
# 3. Swap them.
#
# Recursion allows us to apply the same logic
# to every smaller subtree.

# Dry Run
#
#         4
#       /   \
#      2     7
#     / \   / \
#    1   3 6   9
#
# Start:
#
# invertTree(4)
#
# First invert the subtree rooted at 2.
#
# Node 1:
# left = None
# right = None
# Swap them.
# Return node 1.
#
# Node 3:
# left = None
# right = None
# Swap them.
# Return node 3.
#
# Node 2:
#
# inverted_left = node 1
# inverted_right = node 3
#
# Swap:
#
# node 2.left = node 3
# node 2.right = node 1
#
# Subtree becomes:
#
#       2
#      / \
#     3   1
#
# Next invert the subtree rooted at 7.
#
# Node 6 returns itself.
# Node 9 returns itself.
#
# Node 7 swaps them:
#
#       7
#      / \
#     9   6
#
# Finally node 4 swaps its two inverted subtrees:
#
#         4
#       /   \
#      7     2
#     / \   / \
#    9   6 3   1

# Time Complexity
# O(n)
#
# Every node is visited exactly once.

# Space Complexity
# O(h)
#
# h is the height of the tree due to the recursion stack.
#
# Worst case: O(n)
# Balanced tree: O(log n)


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # Base case:
        # An empty tree is already inverted.
        if root is None:
            return None

        # Invert both subtrees.
        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        # Swap the inverted subtrees.
        root.left = inverted_right
        root.right = inverted_left

        # Return the same root with updated child links.
        return root