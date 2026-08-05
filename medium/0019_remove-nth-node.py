# Question
# Given the head of a linked list, remove the nth node from the end
# of the list and return its head.
#
# Example:
#
# Input:
# head = 1 -> 2 -> 3 -> 4 -> 5
# n = 2
#
# Output:
# 1 -> 2 -> 3 -> 5

# Approach
# Use two pointers: fast and slow.
#
# 1. Create a dummy node before the head.
# 2. Place both fast and slow at the dummy node.
# 3. Move fast forward by (n + 1) nodes.
# 4. Move both pointers together until fast reaches the end.
# 5. Slow will now be just before the node to delete.
# 6. Skip the target node by changing the next pointer.
# 7. Return dummy.next.

# Why Fast & Slow Pointers?
#
# Instead of finding the length first,
# maintain a gap of n nodes between fast and slow.
#
# When fast reaches the end,
# slow automatically reaches the node before the one
# that must be deleted.
#
# This solves the problem in one traversal.

# Dry Run
#
# head = 1 -> 2 -> 3 -> 4 -> 5
# n = 2
#
# Dummy -> 1 -> 2 -> 3 -> 4 -> 5
#
# Initially:
#
# fast = Dummy
# slow = Dummy
#
# Move fast 3 steps (n + 1)
#
# Dummy -> 1 -> 2
#
# Gap between fast and slow = 2 nodes
#
# Move both together.
#
# Eventually:
#
# Dummy -> 1 -> 2 -> 3 -> 4 -> 5
#                  S              F
#
# Slow is just before node 4.
#
# Delete:
#
# slow.next = slow.next.next
#
# Result:
#
# 1 -> 2 -> 3 -> 5

# Why Dummy Node?
#
# Consider:
#
# head = [1]
# n = 1
#
# We need to delete the first node.
#
# Without a dummy node,
# there is no node before head.
#
# Dummy makes deletion of the head exactly the same
# as deleting any other node.

# Time Complexity
# O(n)
# Only one traversal of the linked list.

# Space Complexity
# O(1)
# Only a few pointer variables are used.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n + 1 steps ahead
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            fast = fast.next
            slow = slow.next

        # Skip the node to be deleted
        slow.next = slow.next.next

        # Return the updated head
        return dummy.next