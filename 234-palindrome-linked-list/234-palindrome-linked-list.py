# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        temp = head
        while(temp):
            s.append(temp.val)
            temp =temp.next
        t = head
        while(t and s):
            if t.val != s.pop():
                return False
            t = t.next
        return True