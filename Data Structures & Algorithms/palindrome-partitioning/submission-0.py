# TC: O(n · 2^n) — there can be up to 2^(n-1) ways to cut the string, and checking/copying substrings can cost up to O(n).
# SC: O(n) auxiliary — recursion depth + current path, excluding output.
# If counting all stored answers too, output space can be O(n · 2^n).
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(substring):
            return substring == substring[::-1]
        
        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                substring = s[start: end + 1]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)

        return res