# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count+=1
            
        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        n = count-n
        for i in range(n):
            if curr.next:
                prev = prev.next
                curr = curr.next
        prev.next = curr.next
        return dummy.next