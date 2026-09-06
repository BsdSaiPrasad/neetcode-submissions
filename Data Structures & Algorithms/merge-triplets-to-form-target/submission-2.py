# TC: O(n)
# SC: O(1)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False, False, False]

        for triplet in triplets:
            if( 
                triplet[0] <= target[0] and 
                triplet[1] <= target[1] and
                triplet[2] <= target[2]
                ):

                for i in range(3):
                    if triplet[i] == target[i]:
                        good[i] = True
        return all(good)

# class Solution:
#     def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
#         max_arr = [False] * len(target)

#         for r in range(len(triplets)):
#             if any(triplets[r][c] > target[c] for c in range(len(target))):
#                 continue

#             for c in range(len(triplets[0])):
#                 if triplets[r][c] == target[c]:
#                     max_arr[c] = True

#         return all(max_arr)