class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        i,j = 0,n-1
        m = 0
        mi,mj=0,0
        while(i<j):
            a = (j-i)*min(h[i],h[j])
            m = max(m,a)
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return m