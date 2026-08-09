#Approach 1 : using Regular expression TC: O(n) — regex cleaning + lowercase + reverse comparison all scan the string. SC: O(n) — cleaned creates a new string of size n, and the reversed string also requires space.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = re.sub(r'[^a-zA-Z0-9]','',s).lower()
#         return cleaned[:] == cleaned[::-1]
#Approach 2 : Two Pointers TC is O(n) because we traverse all the elements and SC is O(1) as we dont need extra memory to store anything other than few variables/pointers.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():    
                return False
            i += 1
            j -= 1

        return True
    # def alphaNum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z')or
    #             ord('a') <= ord(c) <= ord('z')or
    #             ord('0') <= ord(c) <= ord('9'))
