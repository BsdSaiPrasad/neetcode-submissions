# TC O(n · n!)
# There are n! permutations, and copying each complete path costs O(n).
# SC O(n) auxiliary recursion/path space, excluding output.
# If counting all results, output space is O(n · n!).
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return res
