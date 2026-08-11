#TC: O(n) — each character gets added to the set once and removed at most once, so total work stays linear.
#SC: O(n) — in the worst case, all characters are unique, so the set can grow to size n.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res= 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            seen.add(s[r])
            res = max(res, len(seen)) # r - l + 1
        return res


            
        