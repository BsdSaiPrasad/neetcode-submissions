# TC: O(n)  
# Slow and fast pointers traverse the array a few times, but each phase is linear.
# SC: O(1)  
# Only uses pointers (slow, fast), no extra data structures.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow



        