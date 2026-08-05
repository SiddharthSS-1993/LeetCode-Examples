# Question
# Given a binary tree and two nodes p and q,
# return their lowest common ancestor.
#
# The lowest common ancestor is the lowest node in the tree
# that has both p and q in its subtree.
#
# A node is allowed to be an ancestor of itself.
#
# Example:
#
#          3
#        /   \
#       5     1
#      / \   / \
#     6   2 0   8
#        / \
#       7   4
#
# p = 5
# q = 1
#
# Answer = 3
#
# Because node 3 is the lowest node that has
# both 5 and 1 below it.
#
# Another example:
#
# p = 5
# q = 4
#
# Answer = 5
#
# Because node 5 is an ancestor of node 4,
# and a node can be an ancestor of itself.

# Approach
# Use DFS recursion.
#
# For every node:
#
# 1. If the node is None, return None.
# 2. If the node is p or q, return the node.
# 3. Search the left subtree.
# 4. Search the right subtree.
# 5. If both left and right return a node,
#    the current node is the lowest common ancestor.
# 6. If only one side returns a node,
#    return that node upward.
# 7. If neither side finds p or q, return None.

# Why This Works
#
# Each recursive call asks:
#
# "Did I find p or q in this subtree?"
#
# Possible answers:
#
# None  -> neither node was found
# p     -> p was found
# q     -> q was found
# LCA   -> both were found below this node
#
# If p is found on one side and q is found on the other side,
# the current node is where their paths meet.

# Dry Run
#
#          3
#        /   \
#       5     1
#      / \   / \
#     6   2 0   8
#
# p = 5
# q = 1
#
# Start at node 3.
#
# Search left:
#
# Node 5 is equal to p,
# so return node 5 immediately.
#
# left_result = 5
#
# Search right:
#
# Node 1 is equal to q,
# so return node 1 immediately.
#
# right_result = 1
#
# Both sides returned a node.
#
# Therefore node 3 is the lowest common ancestor.
#
# Return node 3.

# Second Dry Run
#
# p = 5
# q = 4
#
# Start at node 3.
#
# Search left:
#
# Node 5 is equal to p,
# so return node 5.
#
# Search right:
#
# Neither 5 nor 4 exists in the right subtree,
# so return None.
#
# At node 3:
#
# left_result = 5
# right_result = None
#
# Return node 5 upward.
#
# Final answer = 5.

# Time Complexity
# O(n)
#
# In the worst case, every node is visited once.

# Space Complexity
# O(h)
#
# h is the height of the tree due to recursion.
#
# Balanced tree: O(log n)
# Worst case: O(n)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Nothing found in an empty subtree.
        if root is None:
            return None

        # If the current node is p or q,
        # return it as a possible ancestor.
        if root == p or root == q:
            return root

        # Search both subtrees.
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        # p and q were found on different sides.
        # Therefore, the current node is their LCA.
        if left_result and right_result:
            return root

        # If one side found a node, return it.
        # If neither side found anything, this returns None.
        return left_result if left_result else right_result