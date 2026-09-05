# TC: O(1) because exactly 32 iterations.
# SC: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1 # get the last bit
            res = (res << 1) | bit # left shift res by 1 to make space for the last bit 
            n = n >> 1 # right shift n by 1 to remove the bit we just processed.
        return res
