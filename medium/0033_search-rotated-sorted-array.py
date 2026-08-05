# Question
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot.
#
# Example:
# Original : [0,1,2,4,5,6,7]
# Rotated : [4,5,6,7,0,1,2]
#
# Given the rotated array nums and an integer target,
# return the index of target if it exists.
# Otherwise, return -1.
#
# The algorithm must run in O(log n) time.

# Approach
# 1. Perform Binary Search.
# 2. Find the middle element.
# 3. One half of the array will always be sorted.
# 4. Check whether the target lies inside the sorted half.
# 5. If yes, search that half.
# 6. Otherwise, search the other half.
# 7. Continue until the target is found or the search space becomes empty.

# Why Binary Search?
# Although the array is rotated, one side of every search window
# is always sorted.
#
# By identifying the sorted half, we can determine
# which half can safely be discarded.
#
# Example:
#
# nums = [4,5,6,7,0,1,2]
# target = 0
#
# left = 0
# right = 6
#
# mid = 3
# nums[mid] = 7
#
# Left half:
# [4,5,6,7]
# is sorted.
#
# Target 0 is not inside this range.
#
# Therefore search the right half.
#
# left = 4
# right = 6
#
# mid = 5
# nums[mid] = 1
#
# Right half:
# [0,1,2]
# is sorted.
#
# Target lies inside this range.
#
# Continue searching until target is found.

# Time Complexity
# O(log n)
# Binary Search removes half of the search space every iteration.

# Space Complexity
# O(1)
# Only constant extra memory is used.


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target lies inside left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Search right half
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target lies inside right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Search left half
                else:
                    right = mid - 1

        # Target not found
        return -1