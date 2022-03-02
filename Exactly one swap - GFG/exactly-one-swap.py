#User function Template for python3
class Solution:
    def countStrings(self, S): 
        #code here
        res = len(S)*(len(S)-1)//2 
        d = {}
        for i in S:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        rep = 0
        for k,v in d.items():
            rep+=v*(v-1)//2
        if rep>0:
            res+=1
        return res-rep

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends