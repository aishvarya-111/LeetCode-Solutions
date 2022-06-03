#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,a, n, s):
        if(a[0]==s):
            return [1,1]
        i,j = 0,0
        ss = a[0]
        while(j<n):
            if(ss<s):
                j+=1
                if(j<n):
                    ss+=a[j]
                
            else:
                ss-=a[i]
                i+=1
            
            if(ss==s):
                return [i+1,j+1]
                
            
        return [-1]
        
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends