#TC O(n · 2^n) where n is for path.copy() of each subset and 2^n subsets SC: O(n) auxiliary space, O(2^n) for output list
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if index == len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])
        return res
        