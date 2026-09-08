# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         dp = [0] * len(cost)

#         dp[0] = cost[0]
#         dp[1] = cost[1]

#         for i in range(2, len(cost)):
#             dp[i] = cost[i] + min(dp[i-1], dp[i-2])

#         return min(dp[-1], dp[-2])
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current

        return min(prev1, prev2)