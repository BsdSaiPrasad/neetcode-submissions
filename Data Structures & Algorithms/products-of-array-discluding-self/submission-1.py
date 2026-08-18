# Approach 1 TC is O(n), separate arrays for prefix, suffix, res so O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix = [1] * n
#         suffix = [1] * n
#         res = []

#         product = 1
#         for i in range(n):
#             prefix[i] = product
#             product = product * nums[i]
#         product = 1
#         for i in range(n - 1, -1, -1):
#             suffix[i] = product
#             product = product * nums[i]
#         for i in range(n):
#             res.append(prefix[i] * suffix[i])
#         return res

# Approach 2 TC is O(n) we traverse nums twice (one pass for prefix products and one pass for suffix products).only one array for res, this array is the one the problem asked us to return and is not considered additional memory SC O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        n = len(nums)
        product = 1
        for i in range(n):
            res[i] = product
            product = product * nums[i]
        product = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * product
            product = product * nums[i]
        return res

        