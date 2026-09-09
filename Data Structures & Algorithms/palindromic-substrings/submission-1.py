# TC: O(n^2)
# SC: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            
            #odd length
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count = count + 1

                left = left - 1
                right = right + 1
            
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count = count + 1

                left = left - 1
                right = right + 1

        return count
                