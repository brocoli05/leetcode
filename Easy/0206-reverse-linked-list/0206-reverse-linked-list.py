# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## using recursion
        if head is None or head.next is None:
            return head
        new_tail = head.next
        new_head = self.reverseList(new_tail)
        new_tail.next = head
        head.next = None
        
        return new_head
