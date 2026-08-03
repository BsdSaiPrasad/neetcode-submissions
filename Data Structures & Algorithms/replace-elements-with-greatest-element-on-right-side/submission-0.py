class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        if len(arr) == 0:
            return 
        for i in range(len(arr)-1):
            max_num = max(arr[i+1:])
            res.append(max_num)
        res.append(-1)
        return res
            
                


        