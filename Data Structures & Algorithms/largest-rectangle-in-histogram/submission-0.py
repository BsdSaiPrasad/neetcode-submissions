# TC: O(n)
# Each bar is pushed onto the stack once and popped at most once.
# Even though there is a while inside the for, total pops across the whole algorithm are at most n.
# SC: O(n) for storing in stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, old_height = stack.pop()

                width = i - index
                area = old_height * width
                max_area = max(area, max_area)

                start = index

            stack.append((start, height))

        n = len(heights)
        for start, height in stack:
            width = n - start
            area = height * width
            max_area = max(area, max_area)
        
        return max_area