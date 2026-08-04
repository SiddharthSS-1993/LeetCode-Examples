
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

### Array Except Self  
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
</details>

<details><summary>Strings</summary>

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
</details>
