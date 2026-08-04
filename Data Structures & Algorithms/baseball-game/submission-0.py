#Repeat: we should store the scores of a baseball game. we start with empty record. we are given a list of operations that we must apply to the record. 
# An integer x: Record a new score of x.

# '+': Record a new score that is the sum of the previous two scores.

# 'D': Record a new score that is the double of the previous score.

# 'C': Invalidate the previous score, removing it from the record.

#Examples/Edge Cases: Input: ops = ["1","2","+","C","5","D"] Output: 18, Input: ops = ["5","D","+","C"] Output: 15, numbers can be negative

#Approach: Iterate through each operation and update the stack according to its rule. Numbers are added directly, "+" adds the sum of the previous two scores, "C" removes the previous score, and "D" adds double the previous score. Finally, return the sum of all scores in the stack.

#Test - all test cases passed successfully

#Code
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.lstrip("-").isdigit():  
                num = int(op)
                stack.append(num)
            elif op == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
        return sum(stack)







        