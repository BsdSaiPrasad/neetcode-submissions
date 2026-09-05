# Time complexity: O(m*n)
# Space complexity: O(1) extra space., O(m*n) space for the output list.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        while top <= bottom and left <= right:
            #top : left to right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top = top + 1

            #right : top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right = right - 1
            
            #check bounds to avoid duplicates
            if top <= bottom:
                #bottom : right to left
                for j in range(right , left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom = bottom - 1
            
            if left <= right:
                #left : bottom to top
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left]) 
                left = left + 1
        return res

