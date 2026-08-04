# Question
# Given the root of a Binary Search Tree and an integer k,
# return the kth smallest value in the tree.
#
# A BST has the property:
#
# left subtree values < node value < right subtree values
#
# Therefore, an inorder traversal visits values
# in ascending order.

# Approach
# 1. Use iterative inorder traversal with a stack.
# 2. Keep moving left and push nodes onto the stack.
# 3. When there is no more left child:
#       - Pop the top node.
#       - This is the next smallest value.
#       - Decrease k by 1.
# 4. When k becomes 0, return the current node's value.
# 5. Otherwise, move to the right subtree and continue.

# Why Inorder Traversal?
#
# In a BST:
#
# Left -> Root -> Right
#
# visits values in sorted ascending order.
#
# So the kth node visited is the kth smallest value.

# Dry Run
#
#         5
#       /   \
#      3     7
#     / \   / \
#    2   4 6   8
#
# k = 4
#
# Inorder order:
#
# 2, 3, 4, 5, 6, 7, 8
#
# Visit 2 -> k becomes 3
# Visit 3 -> k becomes 2
# Visit 4 -> k becomes 1
# Visit 5 -> k becomes 0
#
# Return 5 immediately.

# Time Complexity
# O(h + k)
#
# We first travel down the height of the tree,
# then process nodes until reaching the kth smallest.
#
# Worst case: O(n)

# Space Complexity
# O(h)
#
# The stack stores nodes along the current path.
#
# Balanced tree: O(log n)
# Worst case: O(n)


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        stack = []
        current = root

        while current or stack:

            # Move as far left as possible.
            while current:
                stack.append(current)
                current = current.left

            # Visit the next smallest node.
            current = stack.pop()

            k -= 1

            # Stop immediately when the kth node is reached.
            if k == 0:
                return current.val

            # Continue with the right subtree.
            current = current.right