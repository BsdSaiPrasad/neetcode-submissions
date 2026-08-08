#approach 1 - brute force , TC O(n^2) because of nested loops, SC O(1) used only loop variables and no extra data structure
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]==nums[j]:
#                     return True
#         return False

#approach 2 sorting/ suboptimal approach, TC O(nlogn) nums.sort() takes O(nlogn) and loop takes O(n) overall O(nlogn), O(n) auxillary space used by timsort    
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1,len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False

# approach 3 optimal TC O(n) creating set(nums) goes through all n elements once and inserts each into the hash set, SC O(n) in the worst case, set stores all n elements
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums_set = set(nums)
#         return len(nums_set) != len(nums)

#approach 4 optimal TC O(n) we go through all elements in nums once, SC O(n) we might store all the elements of nums in seen if no duplicates existed. 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        