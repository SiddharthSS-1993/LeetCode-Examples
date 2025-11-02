
# Easy Level Problems

This section contains documented solutions to LeetCode Easy problems.  
Each entry includes: **problem link, question, intuition, approach, and complexity.**

---
<details><summary>Array</summary>

<br>

### 001. Two Sum  
🔗 https://leetcode.com/problems/two-sum/

**Question:**
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

**Intuition:**  
We want to find 2 numbers that add up to the target. Instead of checking every pair, which can be slow, we can store numbers, we have already seen in a hash map and check if a complement already exists.

**Approach:**  
1. Loop through the array. 
2. Take a note of num(number from array) and i(index of array) using enumerate.
3. Calculate for each num in the array diff = target - num
4. Seen is initially an empty dictionary, if diff is in the keys of seen(initially no), add the index i to a key diff into the seen dictionary.
5. If diff is later found in seen's keys, we have to return seen[diff] which is the 1st index, and durrent index(our result).

**Time Complexity:**
O(n) as we only scan the array once. and dictionary lookups are O(1) on average.  
**Space Complexity:** 
O(n), worst case we store all values of the array into our dictionary.

---
</details>

<details><summary>Strings</summary>

### 0242. Valid Anagram  
🔗 https://leetcode.com/problems/valid-anagram/

**Question:**
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

**Intuition:**  
Two Strings are Anagrams if they contain the same characters with the same frequency.

So instead of sorting, we can store in a dictionary, a count of each character. From the second string, we loop through the second string and mark of characters already seen, subtrscting counts unitl we get the initial dictionary of all keys having value 0.

**Approach:**  
1. First step very important check if the lengths of the 2 strings differ. If so, they cannot be anagrams.
2. Create a frequency dictionary. This dictionary loops through the length of 1st string s, and takes a count(value) of character(key) to the dictionary. 
3. Eg aab has the counts dictionary{"a": 2, "b": 1}
4. we now loop through string 2, we check if character c from string 2 in counts(characters should be present in same numbers in both strings) or count[c] == 0(if we have more counts from string 2, this condition applies), we apply False.
5. If these conditions dont apply andwe loop through the entire string 2, we reach a solution the 2 strings are anagrams. 

**Time Complexity:** 
O(n) One pass over each string
  
**Space Complexity:** 
O(1) for lower case characters or O(k) per unique characters.
---
</details>

