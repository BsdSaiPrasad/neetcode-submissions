class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # to maintain the current maximum seen so far that is the slowest fleet time on top
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse = True)
        for p,s in pairs:
            time = (target - p)/ s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

        


        