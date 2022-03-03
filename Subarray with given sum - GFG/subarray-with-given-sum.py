#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        d = []
        j,su = 0,0
        for i in range(n):
            d.append(arr[i])
            su+=arr[i]
            while(su>s):
                su = su-d[0]
                d = d[1:]
                j+=1
            if su==s:
                break
        if su!=s:
            return [-1]
        return [j+1 , i+1]         

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