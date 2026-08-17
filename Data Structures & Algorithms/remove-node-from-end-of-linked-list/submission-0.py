#TC: O(n) — one traversal to count + one traversal to remove.
#SC: O(1) — only pointers and counters.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        curr = head
        length = 0 
        while curr:
            length += 1
            curr = curr.next

        curr = dummy
        remove_index = length - n

        for _ in range(remove_index):
            curr = curr.next
        
        curr.next = curr.next.next   
            
        return dummy.next
        