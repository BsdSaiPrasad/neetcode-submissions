# - addNum() → TC: heap push/pop/rebalancing costs O(log n)
# - findMedian() → TC: O(1) because we read heap tops
# SC: O(n) because small and large heaps stores all n numbers.
import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] # max_heap
        self.large = [] # min_heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)

        if self.large and self.small[0] > self.large[0]:
            value = heapq.heappop_max(self.small)
            heapq.heappush(self.large, value)

        if len(self.small) > len(self.large) + 1:
            value = heapq.heappop_max(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush_max(self.small, value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(self.small[0])
        return (self.small[0] + self.large[0]) / 2.0
        
        
        