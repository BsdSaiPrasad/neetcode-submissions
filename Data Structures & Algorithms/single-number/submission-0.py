#O(n) TC and O(1) SC
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res