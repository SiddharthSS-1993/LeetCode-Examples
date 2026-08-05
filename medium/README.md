
# Medium Level Problems

This section contains documented solutions to LeetCode Medium problems.  
Each entry includes: **problem link, question, intuition, approach, and complexity.**

---

<details><summary>Array</summary>

### 0033. Search In Rotated Sorted Array  
🔗 https://leetcode.com/problems/search-in-rotated-sorted-array/

**Question**
There is an integer array nums sorted in ascending order (with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot.

Example:
Original : [0,1,2,4,5,6,7]
Rotated : [4,5,6,7,0,1,2]

Given the rotated array nums and an integer target,
return the index of target if it exists.
Otherwise, return -1.

The algorithm must run in O(log n) time.

**Intuition**
Why Binary Search?
Although the array is rotated, one side of every search window is always sorted.

By identifying the sorted half, we can determine
which half can safely be discarded.

**Approach**
1. Perform Binary Search.
2. Find the middle element.
3. One half of the array will always be sorted.
4. Check whether the target lies inside the sorted half.
5. If yes, search that half.
6. Otherwise, search the other half.
7. Continue until the target is found or the search space becomes empty.

Example:

nums = [4,5,6,7,0,1,2]
target = 0

left = 0
right = 6

mid = 3
nums[mid] = 7

Left half:
[4,5,6,7]
is sorted.

Target 0 is not inside this range.

Therefore search the right half.

left = 4
right = 6

mid = 5
nums[mid] = 1

Right half:
[0,1,2]
is sorted.

Target lies inside this range.

Continue searching until target is found.

**Time Complexity**
O(log n)
Binary Search removes half of the search space every iteration.

**Space Complexity**
O(1)
Only constant extra memory is used.

--- 

### 0238. Array Except Self  
🔗 https://leetcode.com/problems/product-of-array-except-self/

**Question:**
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

**Intuition:**  
We need an output array where each position contains the product of all numbers except the one at that index.

A brute-force approach would require multiplying all other elements for every index → O(n²).
We also cannot use division (because if there are zeros, division breaks or becomes undefined).

✅ The key idea:
Instead of recomputing products multiple times, we can compute:

prefix product = product of all elements before index i

suffix product = product of all elements after index i

Then multiply them.

This allows us to solve it in O(n) time without division.

**Approach:**  
Pass 1: Build prefix products (left → right)
We fill the result array with product of all elements before index i.
1. First we initiate result as a number of 1s, as we progress through the array, we multiply result * previous product.
2. Eg [2, 3, 5, 6]:
3. Initially result[0] is 1 as no value before 2. After we move 1 step forward, result[1] is 2, we store this 2 in a variable prefix.
4. Result[2] = result[1]*nums[1] = 6
5. Result[3] = Result[2]nums[2] = 65 = 30
6. After 1st pass our result is [1,2,6,30]
Pass 2: For second pass we start from end a suffix keeps track of all multiplication of nums from reverse.
1. Initially there is no value post 30, so result[3] = 30, suffix is 1
2. As we step back result[2] = reesult[2]suffix(nums[3]) = 66 = 36
3. Result[1] = result[1]suffix(nums[2]nums[3]) = 265 = 60
4. Result[0] = result[0]suffix(nums[1]nums[2]nums[3]) = 1356 = 90.
5. Our final result is [90, 60, 36, 30].

**Time Complexity:**
O(n) # One forward pass + one backward pass  

**Space Complexity:** 
O(1) extra space # We only store prefix/suffix in variables, not arrays
(Output array is not counted as extra space)

---

### 0347. Top K frequent elements  
🔗 https://leetcode.com/problems/top-k-frequent-elements/description/

**Question**
Given an integer array nums and an integer k,
return the k most frequent elements.

You may return the answer in any order.

**Intuition**
Why Bucket Sort?

Maximum possible frequency is len(nums). Instead of sorting by frequency, directly group numbers according to their frequencies. Then simply scan the buckets backwards.

Approach
1. Count the frequency of each number.
2. Create buckets where index = frequency.
3. Place each number into its corresponding bucket.
4. Traverse the buckets from highest frequency
   to lowest.
5. Stop after collecting k elements.

**Time Complexity**
O(n)
Count frequencies: O(n)
Fill buckets: O(n)
Scan buckets: O(n)

Space Complexity
O(n)

---

</details>

<details><summary>Strings</summary>

### 0003. Longest Substring Without Repeated Characters 
🔗 https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

**Question**
Given a string s, return the length of the longest substring without repeating characters.

A substring must be continuous.
Example:
s = "abcabcbb"
Longest substring without repeating characters:
"abc"
Length = 3

**Intuition**
Why Sliding Window?
We need the longest continuous section of the string that satisfies a condition:

"All characters must be unique."
Sliding window lets us expand the valid substring and shrink it only when a duplicate appears.

This avoids checking every possible substring.

**Approach**
Use a sliding window.
1. Keep two pointers:
   left  -> start of the current window
   right -> end of the current window
2. Use a set to store the characters currently inside the window.
3. Move right across the string.
4. If s[right] is already inside the set:
  - remove s[left] from the set
  - move left forward
  - repeat until s[right] is no longer duplicated
5. Add s[right] to the set.
6. Update the maximum window length.

Window length:
right - left + 1

**Dry Run**

s = "abcabcbb"

Start:
left = 0
seen = {}
right = 0, char = 'a'

Add 'a'
Window = "a"
max_length = 1

-------------------------

right = 1, char = 'b'
Add 'b'
Window = "ab"
max_length = 2

-------------------------

right = 2, char = 'c'
Add 'c'
Window = "abc"
max_length = 3

-------------------------

right = 3, char = 'a'
'a' is already in the set.
Remove s[left] = 'a'
Move left to 1
Add the new 'a'

Window = "bca"
max_length remains 3

-------------------------

Continue the same process.

Final answer = 3

**Time Complexity**
O(n)
Each character is added to the set once and removed from the set at most once.

**Space Complexity**
O(min(n, m))
n is the length of the string.
m is the number of possible unique characters.

---

### 0049. Group Anagram  
🔗 https://leetcode.com/problems/group-anagrams/

**Question:**
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

**Intuition:**  
Two words are anagrams if they contain the same characters in the same frequency.
So instead of comparing every string with every other (too slow), we can use a hash map and group words by a common signature.

The key trick
"eat" → sorted → "aet"
"tea" → sorted → "aet"
"ate" → sorted → "aet"

So all anagrams share the same sorted version → we can use this sorted string as the dictionary key.

**Approach:**  
1. Create a dictionary: groups = {}
2. For each word, compute its sorted version: tuple(sorted(word))
3. Use that sorted tuple as the key and append the   original word to the group
4. Return the dictionary values as a list of lists

Eg Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[["eat", "tea", "ate"],
["tan", "nat"],
["bat"]] 

**Time Complexity:** 
O(n·k log k): n = number of strings, k = max length, sorting each word.
  
**Space Complexity:** 
O(n·k): We store all words in the dictionary.

---
</details>

<details><summary>Linked List</summary>

### 0019. Remove nth node From End  
🔗 https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

**Question**
Given the head of a linked list, remove the nth node from the end
of the list and return its head.

Example:

Input:
head = 1 -> 2 -> 3 -> 4 -> 5
n = 2

Output:
1 -> 2 -> 3 -> 5

**Intuition**
Why Fast & Slow Pointers?

Instead of finding the length first,
maintain a gap of n nodes between fast and slow.

When fast reaches the end,
slow automatically reaches the node before the one
that must be deleted.

This solves the problem in one traversal.

**Approach**

Use two pointers: fast and slow.

1. Create a dummy node before the head.
2. Place both fast and slow at the dummy node.
3. Move fast forward by (n + 1) nodes.
4. Move both pointers together until fast reaches the end.
5. Slow will now be just before the node to delete.
6. Skip the target node by changing the next pointer.
7. Return dummy.next.

Dry Run

head = 1 -> 2 -> 3 -> 4 -> 5
n = 2

Dummy -> 1 -> 2 -> 3 -> 4 -> 5

Initially:

fast = Dummy
slow = Dummy

Move fast 3 steps (n + 1)

Dummy -> 1 -> 2

Gap between fast and slow = 2 nodes

Move both together.

Eventually:

Dummy -> 1 -> 2 -> 3 -> 4 -> 5
                   S              F

Slow is just before node 4.

Delete:

slow.next = slow.next.next

Result:

1 -> 2 -> 3 -> 5

Why Dummy Node?

Consider:

head = [1]
n = 1

We need to delete the first node.

Without a dummy node,
there is no node before head.

Dummy makes deletion of the head exactly the same
as deleting any other node.

**Time Complexity**
O(n)
Only one traversal of the linked list.

**Space Complexity**
O(1)
Only a few pointer variables are used.

---
</details>

<details><summary>Tree</summary>

### 0098. Validate Binary Search Tree  
🔗 https://leetcode.com/problems/validate-binary-search-tree/

**Question**
Given the root of a binary tree, determine whether it is a valid
Binary Search Tree (BST).

A valid BST must satisfy:
1. Every value in the left subtree must be smaller than the current node.
2. Every value in the right subtree must be greater than the current node.
3. Both left and right subtrees must also be valid BSTs.

Duplicate values are not allowed.

**Intuition**
Why In-Order Traversal?

In a valid BST:
- All values in the left subtree are smaller.
- The root comes next.
- All values in the right subtree are larger.

Therefore:
Left -> Root -> Right
produces a strictly increasing sequence.

**Approach**
Use in-order traversal:
Left -> Root -> Right

1. For a valid BST, in-order traversal must produce values in strictly increasing order.
2. Instead of storing all values in a list, keep track of only the previously visited value.
3. If the current value is less than or equal to the previous value, the tree is not a valid BST.

**Dry Run**
Example

        5
      /   \
     3     7
    / \   / \
   2   4 6   8

In-order traversal:
2, 3, 4, 5, 6, 7, 8
Every value is greater than the previous value,
so the tree is valid.

Invalid Example

        5
      /   \
     3     7
          /
         4

In-order traversal:
3, 5, 4, 7

When visiting 4:
4 <= 5
Therefore, the tree is not a valid BST.

**Time Complexity**
O(n)
Every node is visited exactly once.

**Space Complexity**
O(h)
h is the height of the tree because of the recursion stack.
Balanced tree: O(log n)
Worst case: O(n)

---

### 0102. Binary Tree Level Order Traversal  
🔗 https://leetcode.com/problems/binary-tree-level-order-traversal/description/

**Question**
Given the root of a binary tree,
return the level order traversal of its nodes' values.

(i.e., from left to right, level by level.)

Example:

        3
      /   \
     9     20
          /  \
         15   7

Output:

[
  [3],
  [9,20],
  [15,7]
]

**Intuition**
Why BFS?

DFS explores one branch completely.

We need:

Level 1
Level 2
Level 3

Therefore BFS is the natural choice because it processes nodes level-by-level.

**Approach**
1. Use a queue to perform Breadth First Search (BFS).
2. Start by placing the root node into the queue.
3. Process one level at a time.
4. For every node in the current level:
      - Remove it from the queue.
      - Store its value.
      - Add its children to the queue.
5. After processing one level,
   store that level in the answer.
6. Continue until the queue becomes empty.



Dry Run

        3
      /   \
     9     20
          /  \
         15   7

Queue:

[3]

--------------------

Level Size = 1

Remove 3
Level = [3]

Add children:

Queue:
[9,20]

Answer:
[[3]]

--------------------

Level Size = 2

Remove 9
Level = [9]
Remove 20
Level = [9,20]

Add children:

Queue:
[15,7]

Answer:

[[3],[9,20]]

--------------------

Level Size = 2

Remove 15
Remove 7

Queue becomes empty.

Answer:
[[3],[9,20],[15,7]]

**Time Complexity**
O(n)
Every node is visited once.

**Space Complexity**
O(n)
Queue may contain an entire level of the tree.

---

### 0230. kth Smallest Element in a BST  
🔗 https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/


**Question**
Given the root of a Binary Search Tree and an integer k, return the kth smallest value in the tree.

A BST has the property:
left subtree values < node value < right subtree values

Therefore, an inorder traversal visits values in ascending order.

**Intuition**
Why Inorder Traversal?
In a BST:

Left -> Root -> Right

visits values in sorted ascending order. So the kth node visited is the kth smallest value.

**Approach**
1. Use iterative inorder traversal with a stack.
2. Keep moving left and push nodes onto the stack.
3. When there is no more left child:
      - Pop the top node.
      - This is the next smallest value.
      - Decrease k by 1.
4. When k becomes 0, return the current node's value.
5. Otherwise, move to the right subtree and continue.

**Dry Run**

        5
      /   \
     3     7
    / \   / \
   2   4 6   8

k = 4

Inorder order:
2, 3, 4, 5, 6, 7, 8

Visit 2 -> k becomes 3
Visit 3 -> k becomes 2
Visit 4 -> k becomes 1
Visit 5 -> k becomes 0

Return 5 immediately.

**Time Complexity**
O(h + k)
We first travel down the height of the tree,
then process nodes until reaching the kth smallest.
Worst case: O(n)

**Space Complexity
O(h)
The stack stores nodes along the current path.
Balanced tree: O(log n)
Worst case: O(n)

---

### 0236. Lowest Common Ancestor in a BST  
🔗 https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

**Question**
Given a binary tree and two nodes p and q, return their lowest common ancestor.

The lowest common ancestor is the lowest node in the tree that has both p and q in its subtree.

A node is allowed to be an ancestor of itself.

Example:

         3
       /   \
      5     1
     / \   / \
    6   2 0   8
       / \
      7   4

p = 5
q = 1

Answer = 3

Because node 3 is the lowest node that has
both 5 and 1 below it.

Another example:

p = 5
q = 4

Answer = 5

Because node 5 is an ancestor of node 4, and a node can be an ancestor of itself.

**Intuition**
Why This Works

Each recursive call asks:
"Did I find p or q in this subtree?"

Possible answers:
None  -> neither node was found
p     -> p was found
q     -> q was found
LCA   -> both were found below this node

If p is found on one side and q is found on the other side, the current node is where their paths meet.

**Approach**
Use DFS recursion.

For every node:
1. If the node is None, return None.
2. If the node is p or q, return the node.
3. Search the left subtree.
4. Search the right subtree.
5. If both left and right return a node, the current node is    the lowest common ancestor.
6. If only one side returns a node, return that node upward.
7. If neither side finds p or q, return None.

**Dry Run**

         3
       /   \
      5     1
     / \   / \
    6   2 0   8

p = 5
q = 1

Start at node 3.
Search left:
Node 5 is equal to p, so return node 5 immediately.

left_result = 5
Search right:
Node 1 is equal to q,
so return node 1 immediately.

right_result = 1
Both sides returned a node.
Therefore node 3 is the lowest common ancestor.
Return node 3.

Second Dry Run
p = 5
q = 4

Start at node 3.
Search left:
Node 5 is equal to p,
so return node 5.

Search right:
Neither 5 nor 4 exists in the right subtree,
so return None.

At node 3:
left_result = 5
right_result = None
Return node 5 upward.
Final answer = 5.

**Time Complexity**
O(n)
In the worst case, every node is visited once.

**Space Complexity**
O(h)
h is the height of the tree due to recursion.

Balanced tree: O(log n)
Worst case: O(n)

---

</details>
