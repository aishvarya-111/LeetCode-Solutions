# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        while(l1!=None and l2!=None):
            if l1.val<l2.val:
                temp.next = l1
                l1=l1.next
            else:
                temp.next = l2 
                l2 = l2.next 
            temp = temp.next 
        if l1:
            temp.next = l1 
        else:
            temp.next = l2 
        return res.next