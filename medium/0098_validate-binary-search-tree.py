# Question
# Given the root of a binary tree, determine whether it is a valid
# Binary Search Tree (BST).
#
# A valid BST must satisfy:
#
# 1. Every value in the left subtree must be smaller than the current node.
# 2. Every value in the right subtree must be greater than the current node.
# 3. Both left and right subtrees must also be valid BSTs.
#
# Duplicate values are not allowed.

# Approach
# Use in-order traversal:
#
# Left -> Root -> Right
#
# For a valid BST, in-order traversal must produce values
# in strictly increasing order.
#
# Instead of storing all values in a list,
# keep track of only the previously visited value.
#
# If the current value is less than or equal to the previous value,
# the tree is not a valid BST.

# Why In-Order Traversal?
#
# In a valid BST:
#
# - All values in the left subtree are smaller.
# - The root comes next.
# - All values in the right subtree are larger.
#
# Therefore:
#
# Left -> Root -> Right
#
# produces a strictly increasing sequence.

# Example
#
#         5
#       /   \
#      3     7
#     / \   / \
#    2   4 6   8
#
# In-order traversal:
#
# 2, 3, 4, 5, 6, 7, 8
#
# Every value is greater than the previous value,
# so the tree is valid.

# Invalid Example
#
#         5
#       /   \
#      3     7
#           /
#          4
#
# In-order traversal:
#
# 3, 5, 4, 7
#
# When visiting 4:
#
# 4 <= 5
#
# Therefore, the tree is not a valid BST.

# Time Complexity
# O(n)
#
# Every node is visited exactly once.

# Space Complexity
# O(h)
#
# h is the height of the tree because of the recursion stack.
#
# Balanced tree: O(log n)
# Worst case: O(n)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Stores the previously visited value
        # during in-order traversal.
        self.previous = None

        def inorder(node):

            # An empty subtree is valid.
            if node is None:
                return True

            # First, validate the left subtree.
            if not inorder(node.left):
                return False

            # Current value must be strictly greater
            # than the previously visited value.
            if self.previous is not None and node.val <= self.previous:
                return False

            # Update the previous value.
            self.previous = node.val

            # Finally, validate the right subtree.
            return inorder(node.right)

        return inorder(root)