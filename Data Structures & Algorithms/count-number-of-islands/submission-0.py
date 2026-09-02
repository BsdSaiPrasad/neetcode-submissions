# TC: O(R × C)
# Why: every cell is processed at most a constant number of times.
# SC: O(R × C) worst case
# Why: seen may contain every cell, and recursive DFS can also go as deep as R × C in the worst case.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        def dfs(row, col):

            if (
                row < 0 or row >= len(grid) or
                col < 0 or col >= len(grid[0]) or
                grid[row][col] == '0' or
                (row, col) in seen
            ):
                return

            seen.add((row, col))

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in seen:
                    count += 1
                    dfs(row, col)
        return count