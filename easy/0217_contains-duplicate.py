# Question
# Given an integer array nums, return True if any value appears at least twice
# in the array, and return False if every element is distinct.

# Approach
# 1. Create an empty set called 'seen'.
# 2. Traverse the array one element at a time.
# 3. If the current number is already in the set,
#    return True because a duplicate is found.
# 4. Otherwise, add the current number to the set.
# 5. If the loop finishes, no duplicates exist, so return False.

# Why Set?
# A Set stores only unique values.
# It provides O(1) average lookup time.
#
# Example:
#
# nums = [1, 2, 3, 1]
#
# seen = {}
#
# Read 1 -> Add -> {1}
# Read 2 -> Add -> {1, 2}
# Read 3 -> Add -> {1, 2, 3}
# Read 1 -> Already exists -> Return True

# Time Complexity
# O(n)
# We scan the array only once.

# Space Complexity
# O(n)
# In the worst case, all elements are unique and stored in the set.


class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:

            # Duplicate found
            if num in seen:
                return True

            # Store current number
            seen.add(num)

        # No duplicates found
        return False