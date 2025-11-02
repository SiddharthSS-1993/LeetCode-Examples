# Question
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Approach
# 1. First step very important check if the lengths of the 2 strings differ. If so, they cannot be anagrams.
# 2. Create a frequency dictionary. This dictionary loops through the length of 1st string s, and takes a count(value) of character(key) to the dictionary. 
# 3. Eg aab has the counts dictionary{"a": 2, "b": 1}
# 4. we now loop through string 2, we check if character c from string 2 in counts(characters should be present in same numbers in both strings) or count[c] == 0(if we have more counts from string 2, this condition applies), we apply False.
# 5. If these conditions dont apply andwe loop through the entire string 2, we reach a solution the 2 strings are anagrams. 

# Complexity
# - Time complexity:
# O(n) One pass over each string

# - Space complexity:
# O(1) for lower case characters or O(k) per unique characters.

# Code
# python []
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        return True
        
s = "aab"
t = "aba"

sol1 = Solution()
result = sol1.isAnagram(s, t)
print(result)