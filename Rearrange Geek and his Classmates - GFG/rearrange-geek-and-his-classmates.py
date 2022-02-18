#User function Template for python3

class Solution:
    def prank(self, a, n): 
        #code here
        d = {}
        for i in range(n):
            d[a[i]] = i
        
        for k,v in d.items():
            idx = d[v]
            a[idx] = k 
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ob.prank(a, n)
        for i in a:
            print(i,end=" ")
        print()
# } Driver Code Ends