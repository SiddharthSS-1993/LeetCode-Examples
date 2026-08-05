# Question
# Given an array of integers nums sorted in ascending order and an integer target,
# return the index of target if it exists in nums.
# Otherwise, return -1.
#
# The algorithm must run in O(log n) time.

# Approach
# 1. Create two pointers:
#       left  -> start of the search range
#       right -> end of the search range
# 2. Find the middle index of the current search range.
# 3. Compare nums[mid] with the target:
#       a. If they are equal, return mid.
#       b. If nums[mid] is smaller than target, search the right half.
#       c. If nums[mid] is greater than target, search the left half.
# 4. Continue until left becomes greater than right.
# 5. If the target is not found, return -1.

# Why Binary Search?
# The array is already sorted.
# This allows us to eliminate half of the remaining search space
# after every comparison.
#
# Example:
#
# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
#
# left = 0
# right = 5
#
# mid = 2
# nums[mid] = 3
#
# 3 is smaller than 9,
# so discard the left half and search from index 3 to 5.
#
# left = 3
# right = 5
#
# mid = 4
# nums[mid] = 9
#
# Target found at index 4.

# Time Complexity
# O(log n)
# The search space is divided into half after every comparison.

# Space Complexity
# O(1)
# Only a few variables are used regardless of the input size.


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Start of the search range
        left = 0

        # End of the search range
        right = len(nums) - 1

        # Continue while the search range is valid
        while left <= right:

            # Find the middle index
            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Target must be in the right half
            elif nums[mid] < target:
                left = mid + 1

            # Target must be in the left half
            else:
                right = mid - 1

        # Target does not exist in the array
        return -1