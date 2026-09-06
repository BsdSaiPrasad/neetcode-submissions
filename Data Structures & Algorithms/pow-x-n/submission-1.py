# TC: O(log n) — because n is divided by 2 every loop.
# SC: O(1) — only a few variables (x, n, result) are used.

# if exponent is odd:
#     save one x into result

# always:
#     square x
#     cut n in half

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1:
                result = result * x

            x = x * x
            n = n // 2

        return result