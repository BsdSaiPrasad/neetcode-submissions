# Recursion
# TC: O(2^n) — every stair can branch into +1 and +2, so lots of repeated work.
# SC: O(n) — recursion depth can go up to about n.
# class Solution:
#     def climbStairs(self, n: int) -> int:

#         def dfs(num):
#             if num == n:
#                 return 1
#             if num > n:
#                 return 0
#             return dfs(num + 1) + dfs(num + 2)
            
#         return dfs(0)

# Top Down - Memoization , TC O(n), SC O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}
           
#         def dfs(num):
#             if num == n:
#                 return 1
#             if num > n:
#                 return 0
#             if num in memo:
#                 return memo[num]

#             ways = dfs(num + 1) + dfs(num + 2)
#             memo[num] = ways

#             return ways
#         return dfs(0)

#Bottom Up - Tabulation TC O(n), SC O(n)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         dp = [0] * (n + 1)
#         dp[1] = 1
#         dp[2] = 2

#         for i in range(3, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]

# space optimized TC O(n) SC O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2 = 1
        prev1 = 2
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1














