# Question
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Approach
# Pass 1: Build prefix products (left → right)
# We fill the result array with product of all elements before index i.
# 1. First we initiate result as a number of 1s, as we progress through the array, we multiply result * previous product.
# 2. Eg [2, 3, 5, 6]:
# 3. Initially result[0] is 1 as no value before 2. After we move 1 step forward, result[1] is 2, we store this 2 in a variable prefix.
# 4. Result[2] = result[1]*nums[1] = 6
# 5. Result[3] = Result[2]nums[2] = 65 = 30
# 6. After 1st pass our result is [1,2,6,30]
# Pass 2: For second pass we start from end a suffix keeps track of all multiplication of nums from reverse.
# 1. Initially there is no value post 30, so result[3] = 30, suffix is 1
# 2. As we step back result[2] = reesult[2]suffix(nums[3]) = 66 = 36
# 3. Result[1] = result[1]suffix(nums[2]nums[3]) = 265 = 60
# 4. Result[0] = result[0]suffix(nums[1]nums[2]nums[3]) = 1356 = 90.
# 5. Our final result is [90, 60, 36, 30].

# - Complexity
#Time complexity:
# O(n) # One forward pass + one backward pass

# - Space complexity:
# O(1) extra space # We only store prefix/suffix in variables, not arrays
# (Output array is not counted as extra space)

# Code
# python []

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
                res[i] *= suffix
                suffix *= nums[i]
        return res
    
result = Solution()
sol1 = result.productExceptSelf([2, 3, 5, 6])