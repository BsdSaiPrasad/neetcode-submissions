#TC: O(n) — the for loop goes through the prices once, and each iteration does constant-time work: comparisons, subtraction, and max().
#SC: O(1) — we only store a few variables like buy, profit, and max_profit; we don’t create any extra array or data structure that grows with input size.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            sell = sell + 1
        return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#     buy = 0
#     max_profit = 0

#     for sell in range(1, len(prices)):
#         if prices[sell] < prices[buy]:
#             buy = sell
#         else:
#             profit = prices[sell] - prices[buy]
#             max_profit = max(max_profit, profit)

#     return max_profit
        
            

        