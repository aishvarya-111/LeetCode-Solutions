#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        x = [0]*(max(a)+1)
        y = [0]*(max(b)+1) 
        c=0
        for i in range(n):
            x[a[i]]+=1 
            
        for i in range(m):
            y[b[i]]+=1
        
        for i in range(max(max(a),max(b))+1):
            if (i<len(x) and x[i]) or (i<len(y) and y[i]):
                
                c+=1 
        return c
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends