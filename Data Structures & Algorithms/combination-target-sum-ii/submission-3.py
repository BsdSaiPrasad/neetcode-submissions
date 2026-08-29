# TC: O(2^n) worst case — each candidate can be chosen or skipped, though sorting/pruning reduces actual work.
# SC: O(n) auxiliary — recursion depth + path.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)

        return res