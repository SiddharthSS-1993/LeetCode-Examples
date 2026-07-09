# Question
# Given a string s containing only the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# A string is valid if:
# 1. Every opening bracket has a corresponding closing bracket.
# 2. Brackets close in the correct order.
# 3. Every closing bracket has a matching opening bracket.

# Approach
# 1. Create an empty stack to store opening brackets.
# 2. Create a dictionary that maps each closing bracket to its corresponding opening bracket.
# 3. Traverse the string one character at a time.
# 4. If the character is an opening bracket, push it onto the stack.
# 5. If the character is a closing bracket:
#       a. If the stack is empty, return False because there is no opening bracket to match.
#       b. Pop the most recent opening bracket from the stack.
#       c. Compare it with the expected opening bracket from the dictionary.
#       d. If they do not match, return False.
# 6. After processing the entire string, if the stack is empty, all brackets were matched.
#    Otherwise, return False.

# Why Stack?
# A stack follows Last In First Out (LIFO).
# The most recently opened bracket must always be closed first.
# Example:
#
# ([{}])
#
# Push (      Stack: (
# Push [      Stack: ( [
# Push {      Stack: ( [ {
# Pop {       Matches }
# Pop [       Matches ]
# Pop (       Matches )
#
# Stack becomes empty, therefore the string is valid.

# Time Complexity
# O(n)
# Each character is pushed and popped at most once.

# Space Complexity
# O(n)
# In the worst case, all characters are opening brackets and are stored in the stack.


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:

            # If current character is a closing bracket
            if char in pairs:

                # No opening bracket available
                if not stack:
                    return False

                # Remove the latest opening bracket
                last_open = stack.pop()

                # Check if brackets match
                if last_open != pairs[char]:
                    return False

            # Current character is an opening bracket
            else:
                stack.append(char)

        # Valid only if all opening brackets are matched
        return len(stack) == 0