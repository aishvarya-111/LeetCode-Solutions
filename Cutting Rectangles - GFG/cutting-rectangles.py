#User function Template for python3
import math
class Solution:
    def minimumSquares(self, l, b):
        # code here
        g = math.gcd(l,b)
        ans = 0
        a = []
        while True:
            if l*b % g*g == 0:
                ans = l*b//(g*g)
                a = [ans,g]
                break
            g-=1
        return a
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends