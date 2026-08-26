# TC: O(n+m) — each node visited once. SC: O(1) — reuse existing nodes, only a few pointers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iteration TC O(n + m) SC O(1)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         curr = dummy
#         curr1 = list1
#         curr2 = list2
#         while curr1 and curr2:
#             if curr1.val <= curr2.val:
#                 curr.next = curr1
#                 curr1 = curr1.next
#             else:
#                 curr.next = curr2
#                 curr2 = curr2.next
#             curr = curr.next

#         if curr1:
#             curr.next = curr1
#         else:
#             curr.next = curr2

#         return dummy.next

#Recursion TC(n+m) SC O(n+m)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        