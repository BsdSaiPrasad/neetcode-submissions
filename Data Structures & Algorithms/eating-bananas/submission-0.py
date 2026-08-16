# TC binary search over speeds -> O(log M)
# for each speed, scan all piles -> O(n) total = O(n log M) SC is O(1) we are just storing a few variables.
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            hours = 0

            mid = left + (right - left) // 2

            for pile in piles:
                hours += ceil(pile/mid)

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left


        