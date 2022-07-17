class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        if(x==0 or x==1):
            return x
        
        l,r = 1,x 
        while(l<=r):
            m = (l+r)//2
            if m*m > x:
                r = m-1
            elif (m+1)*(m+1) > x:
                ans = m
                break
            else:
                l=m+1
            
        return(ans)