# TC:
# - add() → O(1)
# - count() → O(P)
# SC:
# - O(P)
# where P = number of distinct stored points.
from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0

        for (px, py), freq in self.points.items():

            if abs(px-x) != abs(py-y) or px == x or py == y:
                continue

            total += (
                freq
                * self.points.get((x,py),0)
                * self.points.get((px,y),0)
            )
        return total
