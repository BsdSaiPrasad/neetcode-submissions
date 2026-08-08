#approach 1 sorting TC O(n * klogk) we loop through all n strings and for each string we sort its characters klogk, SC O(nk) the keys tuple(sorted(s)) can take O(k) space each and values store all n strings. 
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         strs_dict = defaultdict(list)
#         for s in strs:
#             strs_dict[tuple(sorted(s))].append(s)
#         return list(strs_dict.values()) # need to conver it to list because the problem expects us to return list not dict
            
# approach 2 character frequency TC O(n * k) outer loop runs for all n strings and for each string we scan its characters(k) so O(n * (k + 26)) is O(n * k), SC is O(n * k) strs_dict stores all the strings grouped together, so n strings and each string has length k 
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            strs_dict[tuple(count)].append(s)
        return list(strs_dict.values())
            



        