# Approach 1 Sorting TC O(nlogn) because counting frequencies takes O(n), then sorting m unique elements takes O(m log m), where m ≤ n. and SC is O(n) Counter, list of frequency pairs, and sorted list can store up to n unique elements.
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         nums_dict = Counter(nums)
#         nums_dict_list = list(nums_dict.items())
#         sorted_data = sorted(nums_dict_list, key = lambda x: x[1])
#         for i in range(k):
#             last_ele = sorted_data.pop()
#             res.append(last_ele[0])
#         return res

#Approach 2 min-heap TC O(nlogk) Count frequencies: O(n) and Each unique number enters/removes heap: O(log k) and SC is O(n) as freq stores n elements, heap stores k and res stores k elements.

# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#         heap = []
#         for num, count in freq.items():
#             heapq.heappush(heap, (count, num))
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         res = []
#         for count, num in heap:
#             res.append(num)
#         return res

#Approach 3 Bucket Sort TC: O(n) — counting frequencies, placing elements into buckets, and scanning buckets all take linear time, SC: O(n) — frequency map + buckets store up to n elements in the worst case.
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            buckets[count].append(num)
        res = []
        for count in range(len(buckets)-1,0,-1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res  