# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            a = head
            b = head.next
            while a is not b:
                a = a.next
                b = b.next.next
            return True
        except:
            return False