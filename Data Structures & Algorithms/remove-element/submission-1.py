#Repeat - an integer array(nums) is given and an integer (val) is given as input. i should remove all the occurrences of that val in the nums array in place. then i should return the number of elements that are not equal to val

#Examples/Edge Cases -
# 1 Input: nums = [3,2,2,3] val = 3 Output: k = 2, nums = [2,2,_,_] , 
# 2 Input: nums = [0,1,2,2,3,0,4,2] val = 2 Output: k = 5 nums = [0,1,3,0,4,_,_,_] ,
# 3 val might not be there in the nums array at all
# 4 nums array can be empty

#Approach - traverse the array from left to right. initialize i = 0, j = 0 and k = 0 where i,j are pointers and k is the count of values which are not equal to the val . when an element is not equal to val we put that element in nums[i] array and increment i and k , and when we are through the list, we then return k which has the count of elements that are not equal and also the nums[i] array with the not equal to val elements. The TC is O(n) because of one for loop traversal and SC is O(1) because of count variable k and i, j . anyways i and k are same, so redundant. so k is commented out. 

#Test- all test cases/ edge cases passed

#Code
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        #k = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
                #k = k + 1
        return i

        
        