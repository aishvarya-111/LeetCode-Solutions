# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #s = []
        #temp = head
        #while(temp):
         #   s.append(temp.val)
          #  temp =temp.next
        #t = head
        #while(t and s):
        #    if t.val != s.pop():
         #       return False
          #  t = t.next
        #return True
        
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        nn = None
        while(slow):
            nn = slow.next
            slow.next = prev
            prev = slow
            slow = nn
        
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True