
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
### 0704. Binary Search  
🔗 https://leetcode.com/problems/binary-search/

**Question**
Given an array of integers nums sorted in ascending order and an integer target,
return the index of target if it exists in nums.
Otherwise, return -1.

The algorithm must run in O(log n) time.

**Intuition**
Why Binary Search?, reducing the time to traverse the entire array after every comparison.

**Approach**
1. Create two pointers:
      left  -> start of the search range
      right -> end of the search range
2. Find the middle index of the current search range.
3. Compare nums[mid] with the target:
      a. If they are equal, return mid.
      b. If nums[mid] is smaller than target, search the right half.
      c. If nums[mid] is greater than target, search the left half.
4. Continue until left becomes greater than right.
5. If the target is not found, return -1.

Example:

nums = [-1, 0, 3, 5, 9, 12]
target = 9

left = 0
right = 5

mid = 2
nums[mid] = 3

3 is smaller than 9,
so discard the left half and search from index 3 to 5.

left = 3
right = 5

mid = 4
nums[mid] = 9

Target found at index 4.

**Time Complexity**
O(log n)
The search space is divided into half after every comparison.

**Space Complexity**
O(1)
Only a few variables are used regardless of the input size.

---
</details>

<details><summary>Strings</summary>

<br>

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
O(n) One pass over each string.
  
**Space Complexity:** 
O(1) for lower case characters or O(k) per unique characters.

---
</details>

<details><summary>Linked List</summary>

<br>

### 0141. Reverse Linked List Cycle  
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

### 0206. Linked List  
🔗 https://leetcode.com/problems/reverse-linked-list/

**Question**
Given the head of a singly linked list, reverse the linked list
and return the new head.

Example:
Input:
1 -> 2 -> 3 -> 4 -> 5 -> None

Output:
5 -> 4 -> 3 -> 2 -> 1 -> None

**Intuition**

Why linked list?
This is an example of a classic linkedlist chain where one node chains to the next.

Why Three Pointers?
When we reverse current.next, we lose access to the remaining list.

**Approach**

Use three pointers:
prev    -> the previous node
current -> the node currently being processed
next_node -> temporarily stores the next node

For every node:
1. Save the next node before changing any links.
2. Reverse the current node's pointer.
3. Move prev one step forward.
4. Move current one step forward.
5. Continue until current becomes None.

At the end, prev points to the new head.

Example:
1 -> 2 -> 3

If we directly change:

1.next = None

then we would lose the reference to node 2.

Therefore, we first save:

next_node = current.next

and only then reverse the pointer.

Dry Run

Original:

1 -> 2 -> 3 -> None

Initial values:

prev = None
current = 1

Iteration 1:
next_node = 2
current.next = prev
None <- 1     2 -> 3

prev = 1
current = 2

Iteration 2:
next_node = 3
current.next = prev

None <- 1 <- 2     3

prev = 2
current = 3

Iteration 3:
next_node = None
current.next = prev

None <- 1 <- 2 <- 3

prev = 3
current = None

The loop ends.
prev is now the new head.

**Time Complexity**
O(n)
We visit every node exactly once.

**Space Complexity**
O(1)
We only use three pointer variables.

---
</details>

<details><summary>Stack</summary>

<br>

### 0020. Valid Parenthesis  
🔗 https://leetcode.com/problems/valid-parentheses/description/

**Question**
Given a string s containing only the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

A string is valid if:
1. Every opening bracket has a corresponding closing bracket.
2. Brackets close in the correct order.
3. Every closing bracket has a matching opening bracket.

**Intuition**
For the string to have a valid parenthesis, each should have equal number of each parenthesis type in the right order.

This is a classic example of a stack, each append while traversing the string, validates the parenthesis type by pushing onto the stack. We can use a dictionary to find the equivalent value pair to each parenthesis. If every push has the right vslue pair pop, and our stack becomes empty. We return true else False

Why Stack?
A stack follows Last In First Out (LIFO).
The most recently opened bracket must always be closed first.
Example:

([{}])

Push (      Stack: (
Push [      Stack: ( [
Push {      Stack: ( [ {
Pop {       Matches } Stack: ( [
Pop [       Matches ] Stack: (
Pop (       Matches ) Stack: 

Stack becomes empty, therefore the string is valid.


**Approach**
1. Create an empty stack to store opening brackets.
2. Create a dictionary that maps each closing bracket to its corresponding opening bracket.
3. Traverse the string one character at a time.
4. If the character is an opening bracket, push it onto the stack.
5. If the character is a closing bracket:
       a. If the stack is empty, return False because there is no opening bracket to match.
       b. Pop the most recent opening bracket from the stack.
       c. Compare it with the expected opening bracket from the dictionary.
       d. If they do not match, return False.
6. After processing the entire string, if the stack is empty, all brackets were matched.
   Otherwise, return False.


**Time Complexity**
O(n)
Each character is pushed and popped at most once.

**Space Complexity**
O(n)
In the worst case, all characters are opening brackets and are stored in the stack.

---
</details>

<details><summary>Set</summary>

<br>

### 0217. Contains Duplicate  
🔗 https://leetcode.com/problems/contains-duplicate/description/

**Question**
Given an integer array nums, return True if any value appears at least twice
in the array, and return False if every element is distinct.

**Intuition**
As we have a case to decide if an array has dupicates, the best approach would be to use Set

Why Set?
A Set stores only unique values.
It provides O(1) average lookup time.

Example:

nums = [1, 2, 3, 1]

seen = {}

Read 1 -> Add -> {1}
Read 2 -> Add -> {1, 2}
Read 3 -> Add -> {1, 2, 3}
Read 1 -> Already exists -> Return True


**Approach**
1. Create an empty set called 'seen'.
2. Traverse the array one element at a time.
3. If the current number is already in the set,
   return True because a duplicate is found.
4. Otherwise, add the current number to the set.
5. If the loop finishes, no duplicates exist, so return False.


**Time Complexity**
O(n)
We scan the array only once.

**Space Complexity**
O(n)
In the worst case, all elements are unique and stored in the set.

---
</details>


