# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        mid = None
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = self.reverse(slow.next)
        slow.next = None
        
        return self.compareLists(head, second_half)
        
    def compareLists(self, head1, head2):        
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True
    
    def reverse(self, head):
        prev = None
        current = head
        next_node = None
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
        