# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        intVal = 0
        len = 0
        current = head
        
        while current is not None:
            len += 1
            current = current.next
        
        current = head
        while current is not None:
            intVal += current.val * (2**(len-1))
            current = current.next
            len -= 1
            
        return intVal