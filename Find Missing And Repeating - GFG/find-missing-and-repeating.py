#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        s1 = (n*(n+1))//2
        s2 = (n*(n+1)*(2*n+1))//6
        
        for i in arr:
            s1-=i
            s2-=(i*i)
        d = s2//s1
        
        m = (s1+d)//2
        r = m-s1
        return [r,m]
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends