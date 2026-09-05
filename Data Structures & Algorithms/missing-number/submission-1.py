# TC: O(n)
# SC: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= i
            missing ^= num
        return missing