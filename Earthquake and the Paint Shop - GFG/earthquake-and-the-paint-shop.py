#User function Template for python3
from collections import OrderedDict
class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
class Solution:
    def sortedStrings(self,N,A):
        #code here
        A.sort()
        d = OrderedDict()
        for i in A:
            if i in d:
                d[i].count+=1
            else:
                d[i]=alphanumeric(i,1)
        S=[]
        for key,value in d.items():
            S.append(value)
        return S

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        a=[]
        for i in range(N):
            x=input()
            a.append(x)
        ob=Solution()
        ans=ob.sortedStrings(N,a)
        for i in ans:
            print(i.name,end=" ")
            print(i.count)
# } Driver Code Ends