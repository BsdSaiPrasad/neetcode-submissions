#approach 1 TC O(n^2) because nums.index() is O(n), SC O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = set()
#         for idx, num in enumerate(nums):
#             needed = target - num
#             if needed in seen:
#                 return [nums.index(needed), idx]
#             seen.add(num)

#approach 2 Optimal TC O(n) because we scan the list once, SC O(n) may need to store up to n numbers and their indices in seen
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], idx]
            seen[num] = idx

