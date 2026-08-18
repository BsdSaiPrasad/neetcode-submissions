# TC: O(N log k)  
# N = total number of nodes across all linked lists  
# Each node is pushed into and popped from the heap once  
# Heap size is at most k (number of lists)  
# Each heap operation = O(log k)
# SC: O(k)  
# Heap stores at most one node from each linked list at a time  
# Output linked list does not count as extra space (we reuse nodes)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        count = 0

        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, count, lst))
                count += 1

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, _, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next

        