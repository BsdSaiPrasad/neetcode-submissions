#Approach : Two Pointers TC: O(n) — each pointer moves at most n steps through the array. SC: O(1) — only using two pointers and variables.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1,j+1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1
         
        