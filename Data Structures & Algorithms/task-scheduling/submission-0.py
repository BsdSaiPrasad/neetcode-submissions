#TC: O(n) — count all tasks once; the rest is over at most 26 task types.
#SC: O(1) — at most 26 uppercase task counts are stored.
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_freq = max(freq.values())

        max_count = 0

        for count in freq.values():
            if count == max_freq:
                max_count += 1
            
        formula = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), formula)
                
        
        
        