# Question
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Approach
# 1. Create a dictionary: groups = {}
# 2. For each word, compute its sorted version: tuple(sorted(word))
# 3. Use that sorted tuple as the key and append the original word to the group
# Return the dictionary values as a list of lists
# Eg Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [["eat", "tea", "ate"],
#  ["tan", "nat"],
#  ["bat"]]

# - Complexity
#Time complexity:
# O(n·k log k): n = number of strings, k = max length, sorting each word

# - Space complexity:
# O(n·k): We store all words in the dictionary

# Code
# python []

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)
        return list(groups.values())