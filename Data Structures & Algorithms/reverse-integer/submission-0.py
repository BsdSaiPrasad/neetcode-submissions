# TC: O(log |x|), effectively O(1) for 32-bit integers
# SC: O(1).
class Solution:
    def reverse(self, x: int) -> int:
        int_min = -2 ** 31
        int_max = 2 ** 31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev_num = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            if rev_num > (int_max - digit) // 10:
                return 0
            
            rev_num = rev_num * 10 + digit
        return sign * rev_num

            