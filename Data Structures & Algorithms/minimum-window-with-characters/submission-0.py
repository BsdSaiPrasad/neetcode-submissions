# TC: O(n) — each pointer moves only forward. SC: O(m) — frequency maps store required/window characters.
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        target_count = Counter(t)
        window_count = {}

        have = 0
        need = len(target_count)

        left = 0

        best_length = float('inf')

        best_left = 0
        best_right = 0

        for right in range(len(s)):
            current_char = s[right]

            window_count[current_char] = window_count.get(current_char, 0) + 1

            if (
                current_char in target_count 
                and window_count[current_char] == target_count[current_char]
                ):
                have += 1

            while have == need:
                # 1. current window is valid, so maybe save it
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left
                    best_right = right
                # 2. try removing the leftmost character
                left_char = s[left]
                window_count[left_char] -= 1
                # 3. did removing it make us lose something required?
                if (left_char in target_count 
                    and window_count[left_char] < target_count[left_char]
                    ):
                    have -= 1
                # 4. shrink window
                left += 1

        if best_length == float('inf'):
            return ""
        return s[best_left: best_right + 1]




        