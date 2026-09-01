# Let n = number of digits. Each digit gives at most 4 letters, so the number of combinations is at most 4^n.
# For the iterative version, you build every final string, and each string has length n, so:
# TC: O(n · 4^n)
# SC: O(n · 4^n) if counting the output list and stored strings.
# For the backtracking version:
# TC: O(n · 4^n)
# SC: O(n) auxiliary recursion depth, but O(n · 4^n) including the output.

#Iteration

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        digits_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
                   }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digits_to_char[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res

#Recursion
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         res = []
#         digits_to_char = {
#             "2" : "abc",
#             "3" : "def",
#             "4" : "ghi",
#             "5" : "jkl",
#             "6" : "mno",
#             "7" : "pqrs",
#             "8" : "tuv",
#             "9" : "wxyz"
#                    }

#         def backtrack(i, curStr):
#             if len(curStr) == len(digits):
#                 res.append(curStr)
#                 return
            
#             for c in digits_to_char[digits[i]]:
#                 backtrack(i+1, curStr + c)
        
#         if digits:
#             backtrack(0, "")

#         return res