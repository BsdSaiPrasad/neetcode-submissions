# TC nlogk(loop through n elements and each heap operation of heap size at most  k costs O(logk)) and SC O(k) heap stores at most k elements
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return heapq.nlargest(k, nums)[-1]

        minHeap = []

        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappushpop(minHeap, num)

        return minHeap[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []

#         for i in range(len(nums)):
#             heapq.heappush(heap, nums[i])

#             if len(heap) > k:
#                 heapq.heappop(heap)
#         return heap[0]
        