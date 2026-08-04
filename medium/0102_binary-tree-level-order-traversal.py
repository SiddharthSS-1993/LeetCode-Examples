# Question
# Given the root of a binary tree,
# return the level order traversal of its nodes' values.
#
# (i.e., from left to right, level by level.)
#
# Example:
#
#         3
#       /   \
#      9     20
#           /  \
#          15   7
#
# Output:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Approach
# 1. Use a queue to perform Breadth First Search (BFS).
# 2. Start by placing the root node into the queue.
# 3. Process one level at a time.
# 4. For every node in the current level:
#       - Remove it from the queue.
#       - Store its value.
#       - Add its children to the queue.
# 5. After processing one level,
#    store that level in the answer.
# 6. Continue until the queue becomes empty.

# Why BFS?
#
# DFS explores one branch completely.
#
# We need:
#
# Level 1
# Level 2
# Level 3
#
# Therefore BFS is the natural choice because
# it processes nodes level-by-level.

# Dry Run
#
#         3
#       /   \
#      9     20
#           /  \
#          15   7
#
# Queue:
#
# [3]
#
# --------------------
#
# Level Size = 1
#
# Remove 3
#
# Level = [3]
#
# Add children:
#
# Queue:
#
# [9,20]
#
# Answer:
#
# [[3]]
#
# --------------------
#
# Level Size = 2
#
# Remove 9
#
# Level = [9]
#
# Remove 20
#
# Level = [9,20]
#
# Add children:
#
# Queue:
#
# [15,7]
#
# Answer:
#
# [[3],[9,20]]
#
# --------------------
#
# Level Size = 2
#
# Remove 15
#
# Remove 7
#
# Queue becomes empty.
#
# Answer:
#
# [[3],[9,20],[15,7]]

# Time Complexity
# O(n)
#
# Every node is visited once.

# Space Complexity
# O(n)
#
# Queue may contain an entire level of the tree.


from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # Empty tree
        if root is None:
            return []

        # Queue for BFS
        queue = deque([root])

        # Final answer
        result = []

        # Continue until all nodes are processed
        while queue:

            # Number of nodes in the current level
            level_size = len(queue)

            # Stores one level
            level = []

            # Process every node in this level
            for i in range(level_size):

                # Remove the front node
                current = queue.popleft()

                # Store its value
                level.append(current.val)

                # Add left child
                if current.left:
                    queue.append(current.left)

                # Add right child
                if current.right:
                    queue.append(current.right)

            # Store the completed level
            result.append(level)

        return result