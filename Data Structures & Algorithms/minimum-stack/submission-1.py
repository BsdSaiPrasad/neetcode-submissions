#Repeat: the task is to design a stack class which does push, pop, top/peek, getMin operations and each function should run in O(1) TC

#Examples/edge cases: Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"] Output: [null,null,null,null,0,null,2,1]

#Approach: Three Approaches
#1. for getMin, we didnt satisfy the required O(1) TC . here we can directly use min function on  the stack to get the min element , so O(n) time because min() scans the whole stack and O(n) space for storing n elements. 

#2 here we used an additional list to temporarily store the popped elements and once we find the min element we push those elements back to the original stack. 

#3 here we used two stacks where one is the original stack and the other is the minStack where we consistently store the min element everytime we push an element and when we pop an element from original stack we also remove the last element from the minStack too. and we return the top most element of minStack as the minimum element of the stack. 

#Test: all approaches successfully passed all the test cases. 

#Code: Below
#Solution1:
# class MinStack:

#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#TC O(n) and SC O(n) for getMin()
    # def getMin(self) -> int:
    #     tmp = []
    #     mini = self.stack[-1]
    #     while(len(self.stack)):
    #         mini = min(mini, self.stack[-1])
    #         tmp.append(self.stack.pop())
    #     while(len(tmp)):
    #         self.stack.append(tmp.pop())
    #     return mini

#Solution 2
#TC O(1) for all operations, SC is O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self)-> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
    
