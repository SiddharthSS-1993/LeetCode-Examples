
# Medium Level Problems

This section contains documented solutions to LeetCode Medium problems.  
Each entry includes: **problem link, question, intuition, approach, and complexity.**

---
<details><summary>Array</summary>

<br>

### 0238. Product Of Array Except Self  
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

