
#approach 2 optimal TC O(1) if n and m are different lengths if lengths are equal, this simplifies to O(n), SC O(1) as we have atmost 26 different characters  
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        return s_dict == t_dict
        