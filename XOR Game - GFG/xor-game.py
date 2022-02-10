#User function Template for python3

class Solution:
    def xorCal(self, k):
        # code here
        if(k%2==0):
            ans = -1
        else:
            if(k==1):
                ans=2
            elif(k==3):
                ans = 1
            elif(k==7):
                ans = 3
            elif(k==15):
                ans = 7
            elif(k==31):
                ans=15
            elif(k==63):
                ans=31
            else:
                ans=-1
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends