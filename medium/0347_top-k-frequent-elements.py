# Question
# Given an integer array nums and an integer k,
# return the k most frequent elements.
#
# You may return the answer in any order.

# Approach
# 1. Count the frequency of each number.
# 2. Create buckets where index = frequency.
# 3. Place each number into its corresponding bucket.
# 4. Traverse the buckets from highest frequency
#    to lowest.
# 5. Stop after collecting k elements.

# Why Bucket Sort?
#
# Maximum possible frequency is len(nums).
#
# Instead of sorting by frequency,
# directly group numbers according to
# their frequencies.
#
# Then simply scan the buckets backwards.

# Time Complexity
# O(n)
#
# Count frequencies: O(n)
# Fill buckets: O(n)
# Scan buckets: O(n)

# Space Complexity
# O(n)


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Count frequency of every number.
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Bucket index represents frequency.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Place every number into its frequency bucket.
        for num, count in frequency.items():
            buckets[count].append(num)

        result = []

        # Traverse from highest frequency
        # to lowest frequency.
        for count in range(len(buckets) - 1, 0, -1):

            for num in buckets[count]:

                result.append(num)

                # Stop once k elements are collected.
                if len(result) == k:
                    return result