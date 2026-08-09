# TC: O(n²) — sorting takes O(n log n), then the outer loop + two pointer scan gives O(n²).
#SC: O(n) — storing the result set (ignoring output storage, extra space is O(1)).
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()
        for i in range(len(sorted_nums) - 2):
            j = i+1
            k = len(sorted_nums) - 1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] == - sorted_nums[i]:
                    res.add((sorted_nums[i],sorted_nums[j],sorted_nums[k]))
                    j= j + 1
                    k = k - 1
                elif sorted_nums[j] + sorted_nums[k] < - sorted_nums[i]:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] > - sorted_nums[i]:
                    k -= 1
        final_res = []
        for lst in res:
            final_res.append(list(lst))
        return final_res



           
        
        