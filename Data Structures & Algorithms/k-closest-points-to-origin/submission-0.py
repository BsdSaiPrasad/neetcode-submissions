# TC O(nlogn(for push) + klogn(for popping k elements)) SC is O(n) , heap stores all points
import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        x1 = 0
        y1 = 0
        for x2, y2 in points:
            
            dist = (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) # or x2**2 + y2**2
            heapq.heappush(heap, (dist, [x2,y2]))

        res = []
        for i in range(k):
            num = heapq.heappop(heap)
            res.append(num[1])

        return res

        



        