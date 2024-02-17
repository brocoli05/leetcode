# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ## using recursion
        if head is None:
            return
        
        head.next = self.removeElements(head.next, val)
        
        if head.val == val:
            return head.next
        else:
            return head
        
#         while head is not None and head.val == val:
#             head = head.next
            
#         current = head
        
#         while current is not None and current.next is not None:
#             if current.next.val == val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
        
#         return head