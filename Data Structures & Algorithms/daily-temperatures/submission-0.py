# TC O(n) for loop is O(n), while operations are O(1) because every index is pushed and popped from stack once.  SC is O(n) res stores the answer for every day, stack can also hold up to n indices. 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res



        
        
            

        