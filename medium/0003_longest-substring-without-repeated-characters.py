# Question
# Given a string s, return the length of the longest substring
# without repeating characters.
#
# A substring must be continuous.
#
# Example:
#
# s = "abcabcbb"
#
# Longest substring without repeating characters:
#
# "abc"
#
# Length = 3

# Approach
# Use a sliding window.
#
# 1. Keep two pointers:
#
#       left  -> start of the current window
#       right -> end of the current window
#
# 2. Use a set to store the characters currently inside the window.
# 3. Move right across the string.
# 4. If s[right] is already inside the set:
#       - remove s[left] from the set
#       - move left forward
#       - repeat until s[right] is no longer duplicated
# 5. Add s[right] to the set.
# 6. Update the maximum window length.
#
# Window length:
#
#       right - left + 1

# Why Sliding Window?
#
# We need the longest continuous section of the string
# that satisfies a condition:
#
# "All characters must be unique."
#
# Sliding window lets us expand the valid substring
# and shrink it only when a duplicate appears.
#
# This avoids checking every possible substring.

# Dry Run
#
# s = "abcabcbb"
#
# Start:
#
# left = 0
# seen = {}
#
# right = 0, char = 'a'
#
# Add 'a'
#
# Window = "a"
# max_length = 1
#
# -------------------------
#
# right = 1, char = 'b'
#
# Add 'b'
#
# Window = "ab"
# max_length = 2
#
# -------------------------
#
# right = 2, char = 'c'
#
# Add 'c'
#
# Window = "abc"
# max_length = 3
#
# -------------------------
#
# right = 3, char = 'a'
#
# 'a' is already in the set.
#
# Remove s[left] = 'a'
# Move left to 1
#
# Add the new 'a'
#
# Window = "bca"
# max_length remains 3
#
# -------------------------
#
# Continue the same process.
#
# Final answer = 3

# Time Complexity
# O(n)
#
# Each character is added to the set once
# and removed from the set at most once.

# Space Complexity
# O(min(n, m))
#
# n is the length of the string.
# m is the number of possible unique characters.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Stores characters currently inside the window.
        seen = set()

        # Start of the current window.
        left = 0

        # Best window length found so far.
        max_length = 0

        # Expand the window using right.
        for right in range(len(s)):

            # Shrink the window until s[right]
            # is no longer duplicated.
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character.
            seen.add(s[right])

            # Update the maximum valid window length.
            max_length = max(
                max_length,
                right - left + 1
            )

        return max_length