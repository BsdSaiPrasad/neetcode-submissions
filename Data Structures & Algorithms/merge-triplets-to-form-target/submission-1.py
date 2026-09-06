# TC: O(n)
# SC: O(1)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_arr = [False] * len(target)

        for r in range(len(triplets)):
            if any(triplets[r][c] > target[c] for c in range(len(target))):
                continue

            for c in range(len(triplets[0])):
                if triplets[r][c] == target[c]:
                    max_arr[c] = True

        return all(max_arr)