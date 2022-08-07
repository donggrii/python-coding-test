# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 내 풀이
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


# 다른 풀이 1 : simple solution with min, max
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


# 다른 풀이 2 : Two-pointers 이용
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


# Test Case 1.
# input: prices = [7, 1, 5, 3, 6, 4]
# output: 5

# Test Case 2.
# input: prices = [7, 6, 4, 3, 1]
# output: 0
