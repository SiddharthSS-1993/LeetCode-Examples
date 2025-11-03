
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
### 0121. Buy Vs Sell Stock  
🔗 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

**Question:**
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

**Intuition:**
To maximize profit, we want to buy at the lowest price before selling at a higher price later. We can track the minimum price seen so far and compute the best possible profit if we sell on each day.

**Approach:**
Start with min price = null(Highest number) and max_profit as 0.
Traverse through the price list. if price < min_price, price becomes the min price.
If this case isnt true, we compare the current max_profit, with difference between price and min price.
If price - min_price > max_profit, that becomes the max profit.
In the end we return maximum profit after the list has been traversed.

**Time complexity:**
O(n) – single pass

**Space complexity:**
O(1), constants space.

---
</details>

<details><summary>Strings</summary>

<br

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

<details><summary>Linked List</summary>

<br

### 0141. Linked List Cycle  
🔗 https://leetcode.com/problems/linked-list-cycle/description/

**Question:**
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

**Intuition:**  
You are given the head of a linked list.
You must return True if the list has a cycle (a node points back to a previous node), else return False.

You cannot use extra space like a list/set (even though it works).
The optimal way is to use Floyd’s Tortoise & Hare Algorithm (fast & slow pointers).

**Approach:**  
We use:
1. slow pointer → moves 1 step
2. fast pointer → moves 2 steps
3. If there is a cycle, fast will eventually meet slow.
4. If there is no cycle, fast will reach None (end of list).
5. Think of this like a race. the faster car if one lap ahead meets the slow car showing the track is cyclic.

**Time Complexity:** 
O(n) — worst case we traverse whole list
  
**Space Complexity:** 
O(1) — no extra data structures used

---
</details>

