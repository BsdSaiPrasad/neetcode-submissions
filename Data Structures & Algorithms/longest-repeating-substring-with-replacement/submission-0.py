#TC: O(n) — `right` pointer moves through the string once, and `left` only moves forward. Each character is added/removed from the window at most once.

#SC: O(1) — the `count` hashmap stores character frequencies. For uppercase English letters, it can have at most 26 keys. (If the character set is unlimited, it becomes O(k) / O(n) depending on input.)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLength = 0
        maxCount = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxCount = max(maxCount, count[s[right]])
            
            winLength = right - left + 1
            if winLength - maxCount > k:
                count[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength


        