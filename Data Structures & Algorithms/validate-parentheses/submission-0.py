#Repeat - return true if the string s has both same opening and closing brackets in correct order else false. 
#Examples/Edge Cases - Input: s = "([{}])" Output: true, Input: s = "[(])" Output: false, s can be empty
#Approach - Create a dictionary where each closing bracket maps to its matching opening bracket. Iterate through the string. If the character is an opening bracket, push it onto the stack. If it is a closing bracket, return False if the stack is empty or if the top of the stack does not match the required opening bracket. Otherwise, pop the matched opening bracket. Finally, return True only if the stack is empty. Time and space complexity is O(n)
#Test - all tests passed successfully 
#Code
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
            }
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack[-1] != s_dict[char]:
                    return False
                stack.pop()
        return not stack
       
            