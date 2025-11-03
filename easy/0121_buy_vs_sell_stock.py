# Question
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Approach
# 1. Start with min price = null(Highest number) and max_profit as 0.
# 2. Traversre through the price list. if price < min_price, price becomes the min price.
# 3. If this case isnt true, we compare the current max_profit, with difference between price and min price. 
# 4. If price - min_price > max_profit, that becomes the max profit.
# 4. In the end we return maximum profit after the list has been traversed. 

# - Time complexity:
# O(n) – single pass

# - Space complexity:
# O(1), constants space.

# Code
#python []

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
               min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
    
result = Solution()
result1 = result.maxProfit([7,1,5,3,6,4])
