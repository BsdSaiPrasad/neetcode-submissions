# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         binary_n = str(bin(n))
#         count = 0
#         for i in binary_n:
#             if i == '1':
#                 count += 1
#         return count

#TC O(1) SC O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n-1) #remember this
            count += 1
        return count
