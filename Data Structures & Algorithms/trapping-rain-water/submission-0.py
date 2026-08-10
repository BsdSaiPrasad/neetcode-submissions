#TC: O(n) — three linear passes through the array
#SC: O(n) — two extra arrays of size n
class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        summ = 0
        for i in range(n):
            potential = min(max_left[i], max_right[i])
            summ = summ + max(0, potential - height[i])
        return summ