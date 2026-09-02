#TC: O(n log n) — because of sorting. The merge scan itself is O(n).
# SC: O(n) if you count the output result.
# Auxiliary SC: O(1) excluding output, ignoring sorting internals.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []

        prev = intervals[0]

        for curr in intervals[1:]:
            if prev[1] >= curr[0]:
                prev[0] = min(prev[0], curr[0])
                prev[1] = max(prev[1], curr[1])
            else:
                result.append(prev)
                prev = curr

        result.append(prev)
        return result
