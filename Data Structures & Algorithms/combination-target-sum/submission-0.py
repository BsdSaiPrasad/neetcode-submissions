# TC: O(n^(T/m)) SC: O(T/m) excluding output. n = len(nums) T = target m = min(nums)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining  < 0:
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i,remaining - nums[i])
                path.pop()

        backtrack(0, target)
        return result
        