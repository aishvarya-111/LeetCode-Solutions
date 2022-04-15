#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,a1,a2,n,m):
        #code here
        p1,p2=n-1,0
        while p1>=0 and p2<m:
            if a1[p1] > a2[p2]:
                a1[p1],a2[p2]=a2[p2],a1[p1]
            p1-=1
            p2+=1
        a1.sort()
        a2.sort()

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends