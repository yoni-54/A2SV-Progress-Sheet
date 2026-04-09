# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        swap = dummy
        while swap.next and swap.next.next:
            first = swap.next
            second = swap.next.next

            first.next = second.next
            second.next = first
            swap.next = second

            swap = first
        return dummy.next
