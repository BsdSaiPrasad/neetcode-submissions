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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict =  {}
        s1_len = len(s1)
        for s in s1:
            s1_dict[s] = s1_dict.get(s, 0) + 1
        
        for l in range(len(s2) - s1_len + 1):
            s2_dict = {}
            s2_temp = s2[l: l + s1_len]
            for s in s2_temp:
                s2_dict[s] = s2_dict.get(s, 0) + 1
            if s1_dict == s2_dict:
                return True
        return False

        
        