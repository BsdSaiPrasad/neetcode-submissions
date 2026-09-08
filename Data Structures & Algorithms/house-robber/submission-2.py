# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
        # prev_first = nums[0]
        # prev_second = nums[1]

        # for i in range(2, len(nums)):
        #     if i % 2 == 0:
        #         prev_first += nums[i]
        #     elif i % 2 == 1:
        #         prev_second += nums[i]
        
        # return max(prev_first, prev_second)
# TC O(n) SC O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]