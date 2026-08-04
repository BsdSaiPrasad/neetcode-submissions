# Approach - nums + nums: Python creates a new list, copies all elements from the first nums, then copies them again from the second nums.
#nums * 2: Python creates a new list by repeating the references inside nums two times.
#[1, 2] + [1, 2]  = [1, 2, 1, 2]
#[1, 2] * 2       = [1, 2, 1, 2]
#Both take O(n) time and O(n) extra space. we dont consider constants. 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums * 2
        return nums + nums