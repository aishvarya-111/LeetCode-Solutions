# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,curr,prev):
        if not curr:
            return prev
        temp = curr.next
        curr.next = prev 
        return self.rev(temp,curr)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev = head,None
        return self.rev(curr,prev)
    
    
        #curr = head
        #prev = None 
        #while curr:
          #  temp = curr.next 
          #  curr.next = prev 
          #  prev = curr 
          #  curr = temp
        #return prev 
    