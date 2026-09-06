#TC O(n) SC O(1)

# [left, right] = all places reachable with current jumps
# scan them all -> find farthest next reach
# move to next level -> jumps += 1
# The moment the last index becomes reachable, that is the first jump level that can reach it.

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            jumps = jumps + 1
            
        return jumps