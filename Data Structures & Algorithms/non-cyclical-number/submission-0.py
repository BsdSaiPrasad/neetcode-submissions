# TC: O(log n) per transformation, because extracting all digits takes proportional time to the number of digits.
# SC: O(k) where k is the number of distinct values stored in seen.
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total = total + digit * digit
                n = n // 10
            n = total
        return True

