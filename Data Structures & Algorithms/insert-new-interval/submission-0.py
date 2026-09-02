# TC: O(n) — we scan the intervals once.
# SC: O(n) if counting the output list.
# Auxiliary SC: O(1) excluding the output.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      

        result = []
        for start, end in intervals:
            # Case 1: current interval is completely before newInterval
            if end < newInterval[0]:
                result.append([start, end])

            # Case 2: current interval is completely after newInterval
            elif start > newInterval[1]:
                result.append(newInterval)
                newInterval = [start, end]

            # Case 3: overlap
            else: 
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        result.append(newInterval)

        return result

        

