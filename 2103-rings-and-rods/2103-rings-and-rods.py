class Solution:
    def countPoints(self, rings: str) -> int:
        l=["","","","","","","","","",""]
        c=0
        for i in range(1,len(rings),2):
            l[int(rings[i])]+=rings[i-1]
            
        for i in l:
            if 'R' in i and 'G' in i and 'B' in i:
                c+=1
        return c