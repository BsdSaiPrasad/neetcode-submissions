# Repeat - the array will be of 1's and 0's, i should return the maximum num of consecutive 1's in the array

# Examples/edge cases - Input: nums = [1,1,0,1,1,1] Output: 3, Input: nums = [1,0,1,1,0,1] Output: 2, array can be entirely 1's or 0's, array can be empty

# Approach - loop over each element and if the element is 1 then add count by 1 and calculate max_count between count and max_count. if its not 1 then make/reset count = 0. max_count will record the maximum count overall, count will calculate the current count. Here TC is O(n)(one loop where we inspect each element), SC is O(1) (it stores the count and max_count)

# Test - all the examples/edge cases passed as mentioned above

# Code
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(count, max_count)
            else:
                count = 0
        return max_count
