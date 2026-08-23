# TC: O(n log n) overall — heapify is O(n), then each smash does heap pops/pushes at O(log n), up to O(n) times.
# SC: O(1)

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            num1 = heapq.heappop_max(heap)
            num2 = heapq.heappop_max(heap)

            if num1 > num2:
                heapq.heappush_max(heap, num1 - num2)

        return heap[0] if heap else 0



        
        