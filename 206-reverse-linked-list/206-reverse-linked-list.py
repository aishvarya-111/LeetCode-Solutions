# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        nn = None
        while(curr):
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        head = prev
        return head