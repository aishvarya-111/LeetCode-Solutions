#User function Template for python3

class Solution:
    def countWays(self, n):
        # code here
        return int(((n+1)*(n+2))/2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.countWays(N))
# } Driver Code Ends