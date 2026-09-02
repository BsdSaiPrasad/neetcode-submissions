class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        count = 0
        prev = intervals[0]

        for curr in intervals[1:]:
            if curr[0] < prev[1]:
                count += 1

                if curr[1] < prev[1]:
                    prev = curr
            else:
                prev = curr

        return count