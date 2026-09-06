# TC: O(n) — one pass to store last positions, one pass to build partitions.
# SC: O(1) — only up to 26 lowercase letters are stored in the hashmap.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        
        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result