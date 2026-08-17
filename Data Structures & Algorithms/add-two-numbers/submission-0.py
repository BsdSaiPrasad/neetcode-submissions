# TC: O(max(n,m)) — visit every node.
# SC: O(max(n,m)) — output list stores result nodes. (Extra working space is O(1).)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        l1_curr = l1
        l2_curr = l2
        while l1_curr or l2_curr or carry:

            val1 = l1_curr.val if l1_curr else 0
            val2 = l2_curr.val if l2_curr else 0
            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10
            
            curr.next = ListNode(digit)
            curr = curr.next
        
            if l1_curr:
                l1_curr = l1_curr.next
            
            if l2_curr:
                l2_curr = l2_curr.next

        return dummy.next

