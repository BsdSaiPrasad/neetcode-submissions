#Brute Force Approach - TC: roughly O(m! × n) there can be m! permutations, and you search for each inside s2
#SC: O(m! × m) — you store all permutations as strings.
# from itertools import permutations
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         perm_s1 = [''.join(p) for p in permutations(s1)]
#         for s in perm_s1:
#             if s in s2:
#                 return True
#         return False

#Brute Force Fixed-Size Window + Frequency Map TC: O(n × m) — there are roughly n windows and rebuilding each window count takes m work.
#SC: O(m) — frequency maps/window hold at most m characters.
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1_dict =  {}
#         s1_len = len(s1)
#         for s in s1:
#             s1_dict[s] = s1_dict.get(s, 0) + 1
        
#         for l in range(len(s2) - s1_len + 1):
#             s2_dict = {}
#             s2_temp = s2[l: l + s1_len]
#             for s in s2_temp:
#                 s2_dict[s] = s2_dict.get(s, 0) + 1
#             if s1_dict == s2_dict:
#                 return True
#         return False

#Optimal Approach TC: O(n) — where n = len(s2). You scan s2 once, and each step only adds/removes one character and compares two Counters. Since the alphabet is bounded for this problem, that comparison is effectively constant time. SC: O(1) — if the input is lowercase English letters, each Counter stores at most 26 keys, so extra space is constant.
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s1_len = len(s1)
        window_counter = Counter()
        for i, c in enumerate(s2):
            window_counter[c] += 1
            if i >= s1_len:
                element_from_left = s2[i - s1_len]
                if window_counter[element_from_left] == 1:
                    del window_counter[element_from_left]
                else:
                    window_counter[element_from_left] -= 1
            if window_counter == s1_counter:
                return True
        return False
        
        