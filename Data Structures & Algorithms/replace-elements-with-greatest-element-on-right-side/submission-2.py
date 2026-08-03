# R array in place/ new array, last element should be replaced with -1, rest should be replaced with greatest element on their right, the current element should not be included when considering for the greatest element. then return the array  

# E Input1: arr = [2,4,5,3,1,2] Output1: [5,5,3,2,2,-1] , Input2: arr = [3,3] Output2: [3,-1]
# array can be empty , can be only one element, can be negative elements

# A approach 
# Brute force : i will traverse from 0 until last element and apply max function on i+1 to the last element each time and append it to the new array and once looped through all the elements i will append the -1 to the new array as the last element. TC n^2 (because one loop and slicing/max func), SC n (we are storing in new array)
# Optimal - i will traverse from last element to the first element , will store the max_val as -1 to assign the value to the last element, and i will store the current element(current) and will assign the max_val to the current ith element(arr[i]), and now calculate the max element amongst the current value and max_value and update the max_value. this will replace the values in-place and will return the array. 

# C - below
# T - test against examples discussed, and the edge cases 

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_val
            max_val = max(current, max_val)
        return arr
