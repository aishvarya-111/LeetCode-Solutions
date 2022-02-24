#User function Template for python3

class Solution:
    def primeDivision(self, N):
        def isprime(n):
            for i in range(2,n//2+1):
                if n%i==0:
                    return 0
            return 1
        
        for i in range(2,N//2+1):
            if isprime(i) and isprime(N-i):
                a = [i,N-i]
                return a

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends