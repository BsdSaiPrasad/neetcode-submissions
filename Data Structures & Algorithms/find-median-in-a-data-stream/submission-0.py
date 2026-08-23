# - addNum() → TC: O(1), just append
# - findMedian() → TC: O(n log n) because of sorting
# SC: O(n) because self.arr stores all numbers.
class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n// 2]
        else:
            return(self.arr[n//2 - 1] + self.arr[(n//2)]) / 2

        
        