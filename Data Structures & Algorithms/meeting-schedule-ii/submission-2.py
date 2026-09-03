# TC: O(n log n) — sorting takes O(n log n), and each heap push/pop is O(log n).
# SC: O(n) — in the worst case, all meetings overlap, so the heap stores n end times.

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)

        heap = []
        
        for meeting in intervals:
            if heap and meeting.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, meeting.end)

        return len(heap)






        # rooms_needed = 1
        # for curr in intervals[1:]:
        #     if curr.start < prev.end:
        #         rooms_needed += 1
        #         prev = curr
        # return rooms_needed
