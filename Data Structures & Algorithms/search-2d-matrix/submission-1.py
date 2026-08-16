# TC is O(log(rows × cols)) — binary search over all elements. O(m*n) m is no of rows and n is no of cols. SC is O(1) — only pointers and index variables.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols
        left = 0
        right = n - 1

        while(left <= right):
            mid = left + (right - left) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False