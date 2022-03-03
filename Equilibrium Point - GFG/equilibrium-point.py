# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        if N==1:
            return 1
        s,s1,s2 = sum(A),0,0
        for i in range(N):
            s2 = s-s1-A[i]
            if s2==s1:
                return i+1 
            s1 = s1+A[i]
        return -1


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends