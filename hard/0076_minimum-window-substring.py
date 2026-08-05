# Question
# Given two strings s and t, return the smallest substring of s
# that contains every character from t, including duplicate characters.
#
# If no such substring exists, return "".
#
# Example:
#
# s = "ADOBECODEBANC"
# t = "ABC"
#
# Output:
# "BANC"

# Approach
# Use a sliding window with two frequency dictionaries.
#
# 1. Count how many times each character is required in t.
# 2. Expand the window using the right pointer.
# 3. Track the frequency of characters inside the current window.
# 4. Track how many required character conditions are currently satisfied.
# 5. Once all conditions are satisfied:
#       - Record the window if it is the smallest so far.
#       - Shrink the window from the left.
# 6. Stop shrinking when removing a character makes the window invalid.
# 7. Continue expanding and shrinking until the string is processed.

# Why Use "formed" and "required"?
#
# Suppose:
#
# t = "AABC"
#
# need:
#
# A -> 2
# B -> 1
# C -> 1
#
# required = 3
#
# required counts the number of unique character conditions,
# not the total number of characters.
#
# A condition becomes satisfied only when the window contains
# exactly the required number of that character.
#
# Example:
#
# window["A"] becomes 2
#
# Now the condition for A is satisfied,
# so formed increases by 1.
#
# The complete window is valid when:
#
# formed == required

# Dry Run
#
# s = "ADOBECODEBANC"
# t = "ABC"
#
# need = {
#     "A": 1,
#     "B": 1,
#     "C": 1
# }
#
# required = 3
#
# Expand right:
#
# "A"
# formed = 1
#
# "ADOB"
# formed = 2
#
# "ADOBEC"
# formed = 3
#
# The window is now valid.
#
# Record:
#
# "ADOBEC"
#
# Shrink from the left:
#
# Remove A
#
# A count becomes 0,
# which is below the required count.
#
# formed becomes 2.
#
# Window is invalid again.
#
# Continue expanding until:
#
# "CODEBANC"
#
# Then shrink:
#
# "ODEBANC"
# "DEBANC"
# "EBANC"
# "BANC"
#
# "BANC" is valid and shorter than "ADOBEC".
#
# Final answer = "BANC"

# Time Complexity
# O(n + m)
#
# n is the length of s.
# m is the length of t.
#
# Each character in s is visited at most twice:
# once by right and once by left.

# Space Complexity
# O(m)
#
# The dictionaries store the required characters from t.


from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # A valid window is impossible in these cases.
        if not s or not t or len(t) > len(s):
            return ""

        # Frequency of every required character.
        need = Counter(t)

        # Frequency of characters in the current window.
        window = {}

        # Number of unique character conditions required.
        required = len(need)

        # Number of unique character conditions currently satisfied.
        formed = 0

        # Left edge of the window.
        left = 0

        # Stores:
        # window length, start index, end index
        best = (float("inf"), 0, 0)

        # Expand the window using right.
        for right in range(len(s)):
            char = s[right]

            # Add the current character to the window.
            window[char] = window.get(char, 0) + 1

            # A required character condition has just become satisfied.
            if char in need and window[char] == need[char]:
                formed += 1

            # The window contains all required characters.
            while formed == required:

                # Update the best answer.
                window_length = right - left + 1

                if window_length < best[0]:
                    best = (window_length, left, right)

                left_char = s[left]

                # Remove the leftmost character.
                window[left_char] -= 1

                # A required condition is no longer satisfied.
                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    formed -= 1

                # Move the left edge forward.
                left += 1

        # No valid window was found.
        if best[0] == float("inf"):
            return ""

        return s[best[1]:best[2] + 1]