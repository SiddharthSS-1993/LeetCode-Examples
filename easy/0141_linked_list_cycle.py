# Question
# Given head, the head of a linked list, determine if the
# linked list has a cycle in it.
# There is a cycle in a linked list if there is some node
# in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Approach
# We use:
# 1. slow pointer → moves 1 step
# 2. fast pointer → moves 2 steps
# 3. If there is a cycle, fast will eventually meet slow.
# 4. If there is no cycle, fast will reach None (end of
# list).
# Think of this like a race. the faster car if one lap
# ahead meets the slow car showing the track is cyclic.

# - Time complexity:
# O(n) — worst case we traverse whole list


# - Space complexity:
# O(1) — no extra data structures used

# Code
# python []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2 # cyclic

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

result = Solution()
result1 = result.hasCycle(n1)