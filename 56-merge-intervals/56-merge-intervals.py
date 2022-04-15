class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        if len(l)==0:
            return l
        l.sort()
        t = l[0]
        a=[]
        for i in l:
            if i[0]<=t[1]:
                t[1] = max(i[1],t[1])
            else:
                a.append(t)
                t = i
        a.append(t)
        return a