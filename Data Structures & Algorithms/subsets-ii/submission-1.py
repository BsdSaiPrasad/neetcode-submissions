class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(index, path):
            if index == len(nums):
                res.add(tuple(sorted(path.copy())))
                return
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])
        return [list(x) for x in res]

        