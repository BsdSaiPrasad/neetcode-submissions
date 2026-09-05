# TC: O(n log n) worst case, because for each number you may remove up to O(log n) set bits.
# SC: O(n) because res stores n + 1 answers.
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            while i:
                i = i & (i-1)
                count += 1
            res.append(count)
        return res

