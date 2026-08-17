# TC: O(n) because slow/fast visit at most a linear number of nodes before either fast hits None or they meet.
# SC: O(1) because you only use two pointers: slow and fast.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
       
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True    
        return False 
            
        