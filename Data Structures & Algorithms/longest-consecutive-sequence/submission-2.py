#TC: O(n) - each number is added to the set once, and each consecutive sequence is traversed only from its starting number. SC: O(n) - the hash set stores all numbers.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        if len(nums) == 0:
            return 0
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    count = count + 1
                    num = num + 1
                max_count = max(max_count, count)
            
        return max_count
        
        
