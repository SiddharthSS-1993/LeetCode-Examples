# Question
# Given the head of a singly linked list, reverse the linked list
# and return the new head.
#
# Example:
#
# Input:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
#
# Output:
# 5 -> 4 -> 3 -> 2 -> 1 -> None

# Approach
# Use three pointers:
#
# prev    -> the previous node
# current -> the node currently being processed
# next_node -> temporarily stores the next node
#
# For every node:
# 1. Save the next node before changing any links.
# 2. Reverse the current node's pointer.
# 3. Move prev one step forward.
# 4. Move current one step forward.
# 5. Continue until current becomes None.
#
# At the end, prev points to the new head.

# Why Three Pointers?
# When we reverse current.next, we lose access to the remaining list.
#
# Example:
#
# 1 -> 2 -> 3
#
# If we directly change:
#
# 1.next = None
#
# then we would lose the reference to node 2.
#
# Therefore, we first save:
#
# next_node = current.next
#
# and only then reverse the pointer.

# Dry Run
#
# Original:
#
# 1 -> 2 -> 3 -> None
#
# Initial values:
#
# prev = None
# current = 1
#
# Iteration 1:
#
# next_node = 2
# current.next = prev
#
# None <- 1     2 -> 3
#
# prev = 1
# current = 2
#
# Iteration 2:
#
# next_node = 3
# current.next = prev
#
# None <- 1 <- 2     3
#
# prev = 2
# current = 3
#
# Iteration 3:
#
# next_node = None
# current.next = prev
#
# None <- 1 <- 2 <- 3
#
# prev = 3
# current = None
#
# The loop ends.
# prev is now the new head.

# Time Complexity
# O(n)
# We visit every node exactly once.

# Space Complexity
# O(1)
# We only use three pointer variables.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # No node has been reversed yet
        prev = None

        # Start from the original head
        current = head

        while current:

            # Save the next node before changing the link
            next_node = current.next

            # Reverse the current node's pointer
            current.next = prev

            # Move prev forward
            prev = current

            # Move current forward
            current = next_node

        # prev is the new head of the reversed list
        return prev