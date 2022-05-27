class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ad: int) -> int:
        d = []
        for i in range(len(capacity)):
            d.append(capacity[i]-rocks[i])
        d.sort()
        c = 0
        for i in range(len(d)):
            if ad>0 and d[i]>0 and ad>=d[i]:
                ad = ad-d[i]
                d[i]=0
                c+=1 
            elif d[i]==0:
                c+=1
        return c
            