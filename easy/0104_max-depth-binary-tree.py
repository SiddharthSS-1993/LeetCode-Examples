# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Base case:
        # If there is no node,
        # the depth is zero.
        if root is None:
            return 0

        # Find the maximum depth
        # of the left subtree.
        left_depth = self.maxDepth(root.left)

        # Find the maximum depth
        # of the right subtree.
        right_depth = self.maxDepth(root.right)

        # Current node adds one level.
        return 1 + max(left_depth, right_depth)
        