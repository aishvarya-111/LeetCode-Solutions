class Solution:
    def isHappy(self, n: int) -> bool:
        def sq(n):
            n = sum([int(i)**2 for i in str(n)])
            return n
        
        slow = sq(n)
        fast = sq(sq(n))
        while slow!=fast and fast!=1:
            slow = sq(slow)
            fast = sq(sq(fast))
            
        return fast==1