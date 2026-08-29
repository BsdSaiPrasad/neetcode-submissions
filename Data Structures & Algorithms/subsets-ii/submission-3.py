# TC: O(n · 2^n) — up to 2^n subsets, and copying each subset can cost up to O(n).
# SC: O(n) auxiliary — recursion depth + current path.
# If counting the output too: O(n · 2^n).

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtrack(start):
            res.append(path.copy())
                
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res

        