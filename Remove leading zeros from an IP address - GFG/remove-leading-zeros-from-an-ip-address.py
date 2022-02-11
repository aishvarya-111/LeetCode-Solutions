#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        # code here
        n = list(s.split('.'))
        for i in range(len(n)):
            n[i]=str(int(n[i]))
        r = '.'
        r=r.join(n)
        return r

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends