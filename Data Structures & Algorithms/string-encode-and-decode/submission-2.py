#Approach TC is O(n) because encode() goes through every string and every character when joining - O(n) decode() moves i and j through the encoded string once - O(n) and SC is O(n) because we store the encoded string and the decoded list of strings, both proportional to the input size.
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
      
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i < len(s)):
            j = i
            while(s[j] != '#'):
                j = j + 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
        