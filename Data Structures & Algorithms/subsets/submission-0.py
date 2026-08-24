#TC O(n · 2^n) where n is for path.copy() of each subset and 2^n subsets SC: O(n) auxiliary space, O(2^n) for output list

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()

            backtrack(index + 1)

        backtrack(0)
        return result
        