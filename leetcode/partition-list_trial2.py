# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            before = ListNode(0)
            after = ListNode(0)
        
            before_ptr = before
            after_ptr = after
        
            current = head
        
            while current:
                if current.val < x:
                    before_ptr.next = current
                    before_ptr = before_ptr.next
                else:
                    after_ptr.next = current
                    after_ptr = after_ptr.next
            
                current = current.next
        
            after_ptr.next = None
        
            before_ptr.next = after.next
        
            return before.next