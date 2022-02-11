class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s,m = 0,10**6
        res=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                ind = list2.index(list1[i])
                s = i+ind
                if(s==m):
                    res.append(list1[i])
                elif(s<m):
                    m=s
                    res=[]
                    res.append(list1[i])
        return res
                    
                    