# TC: O(n log n) because of sorting.
# SC: O(n) for the frequency map.
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for card in sorted(hand):
            if count[card] == 0:
                continue
            
            for next_card in range(card, card + groupSize):
                if count[next_card] == 0:
                    return False
                count[next_card] = count[next_card] - 1

        return True