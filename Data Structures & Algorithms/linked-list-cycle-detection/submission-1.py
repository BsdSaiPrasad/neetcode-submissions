# TC: O(n) because slow/fast visit at most a linear number of nodes before either fast hits None or they meet.
# SC: O(1) because you only use two pointers: slow and fast.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Fast and Slow Pointers TC O(n) SC is O(1)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow = head
        # fast = head
       
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True    
        # return False 

#Hashset TC O(n) SC O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False
        