# TC: O(n) because you do a few linear passes: find middle + reverse second half + merge. O(n) + O(n) + O(n) = O(n).
# SC: O(1) because you only use pointers like slow, fast, prev, first_curr, second_curr, etc. No extra list/hashmap.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_curr = head
        second_curr = slow.next
        slow.next = None
        
        prev = None

        while second_curr:
            next_node = second_curr.next
            second_curr.next = prev
            prev = second_curr
            second_curr = next_node

        second_curr = prev

        while second_curr:
            first_next = first_curr.next
            second_next = second_curr.next
            first_curr.next = second_curr
            second_curr.next = first_next
            first_curr = first_next
            second_curr = second_next
            
        
        

        
        


        