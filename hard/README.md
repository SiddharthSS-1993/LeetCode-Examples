# Hard Level Problems

This section contains documented solutions to LeetCode Hard problems.

Each entry includes: **problem link, question, intuition, approach, and complexity.**

---
<details><summary>Tree</summary>

### 0124. Binary Tree Maximum Path Sum  
🔗 https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

**Question**
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes is connected by an edge.

A path does not need to pass through the root. The path sum is the sum of the values of the nodes in the path.

Return the maximum path sum of any path in the tree.

**Intuition**
Why DFS?

Every node needs information from its left and right subtrees.
DFS naturally solves the smaller subtrees first and then combines their answers to compute the result for the current node.

Unlike Maximum Depth from problem 0104, this problem requires two values:

1. Current Path
   node.val + left_gain + right_gain
   Used to update the global answer.

2. Return Value
   node.val + max(left_gain, right_gain)

   Returned to the parent because a path can continue through
   only one child.

**Approach**
1. Use Depth First Search (DFS) to traverse the tree.
2. For every node, recursively calculate the maximum   contribution from the left and right subtrees.
3. Ignore negative contributions because they decrease the path sum.
4. Calculate the maximum path passing through the current node:
   node.val + left_gain + right_gain
5. Update the global maximum path sum.
6. Return only one branch to the parent:
   node.val + max(left_gain, right_gain)

A parent cannot continue through both branches because a path
cannot split into two directions.

**Dry Run**

        -10
        /  \
       9    20
           /  \
          15   7

Initially start traversing left from Node 10
Node 9

left_gain = 0
right_gain = 0

current_path = 9

maximum_sum = 9
return = 9 + max(0,0) = 9

--------------------------
Traverse back to right of root 10 and then right of 10, 20 and then to the left of 20, 15
Node 15

left_gain = 0
right_gain = 0

current_path = 15
maximum_sum = 15
return = 15 + max(0, 0) = 15

--------------------------
Traverse back to 20 and look into the right of 20, 7
Node 7

left_gain = 0
right_gain = 0

current_path = 7
maximum_sum = 7
return = 7 + max(0,0) = 7

--------------------------
Now that we have max_path for 15 and 7 traverse to 20
Node 20

left_gain = 15
right_gain = 7

current_path = 20 + 15 + 7 = 42

maximum_sum = 42

return = 20 + max(15,7) = 35

--------------------------
Traverse back to root node -10
Node -10
left_gain = 9
right_gain = 35

current_path = -10 + 9 + 35 = 34
maximum_sum remains 42
return = -10 + max(9,35) = 25

Final Answer = 42

--------------------------

**Time Complexity**
O(n)
Every node is visited exactly once(Although we said traverse back to different nodes. it is handled through recursion).

**Space Complexity**
O(h)
h is the height of the tree.
Worst case: O(n)
Balanced tree: O(log n)

---

</details>

<details><summary>Strings</summary>

### 00076. Minimum Window Substring  
🔗 https://leetcode.com/problems/minimum-window-substring/description/

**Question**
Given two strings s and t, return the smallest substring of s that contains every character from t, including duplicate characters.

If no such substring exists, return "".

Example:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"

**Intuition**
Why Use "formed" and "required"?

Suppose:
t = "AABC"

need:
A -> 2
B -> 1
C -> 1

required = 3
required counts the number of unique character conditions, not the total number of characters.

A condition becomes satisfied only when the window contains exactly the required number of that character.

Example:
window["A"] becomes 2
Now the condition for A is satisfied, so formed increases by 1.

The complete window is valid when:
formed == required

**Approach**
Use a sliding window with two frequency dictionaries.
1. Count how many times each character is required in t.
2. Expand the window using the right pointer.
3. Track the frequency of characters inside the current window.
4. Track how many required character conditions are currently satisfied.
5. Once all conditions are satisfied:
    - Record the window if it is the smallest so far.
   - Shrink the window from the left.
6. Stop shrinking when removing a character makes the window invalid.
7. Continue expanding and shrinking until the string is processed.


**Dry Run**
s = "ADOBECODEBANC"
t = "ABC"

need = {
    "A": 1,
    "B": 1,
    "C": 1
}

required = 3

Expand right:
"A"
formed = 1

"ADOB"
formed = 2

"ADOBEC"
formed = 3
The window is now valid.

#Record:
"ADOBEC"

Shrink from the left:
Remove A
A count becomes 0,
which is below the required count.

formed becomes 2.
Window is invalid again.
Continue expanding until:

"CODEBANC"
Then shrink:
"ODEBANC"
"DEBANC"
"EBANC"
"BANC"

"BANC" is valid and shorter than "ADOBEC".
Final answer = "BANC"

**Time Complexity**
O(n + m)
n is the length of s.
m is the length of t.
Each character in s is visited at most twice: once by right and once by left.

**Space Complexity**
O(m)
The dictionaries store the required characters from t.

---

</details>
