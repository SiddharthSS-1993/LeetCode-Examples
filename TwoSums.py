# Question
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Intuition
# We want to find 2 numbers that add up to the target. Instead of checking every pair, which can be slow, we can store numbers, we have already seen in a hash map and check if a complement already exists. 

# Approach
# 1. Loop through the array. 
# 2. Take a note of num(number from array) and i(index of array) using enumerate.
# 3. Calculate for each num in the array diff = target - num
# 4. Seen is initially an empty dictionary, if diff is in the keys of seen(initially no), add the index i to a key diff into the seen dictionary.
# 5. If diff is later found in seen's keys, we have to return seen[diff] which is the 1st index, and durrent index(our result).

# Complexity
# - Time complexity:
# O(n) as we only scan the array once. and dictionary lookups are O(1) on average.

# - Space complexity:
# O(n), worst case we store all values of the array into our dictionary.

# Code
# python []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

nums = [2, 7, 11, 15]
target = 9

# Create a new Object
sol = Solution()
result = sol.twoSum(nums, target)
print(result)