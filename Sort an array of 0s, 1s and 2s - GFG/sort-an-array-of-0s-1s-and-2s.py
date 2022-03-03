#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        a = [0,0,0]
        for i in arr:
            a[i]+=1
        for i in range(a[0]):
            arr[i] = 0
        for i in range(a[0],a[0]+a[1]):
            arr[i] = 1
        for i in range(a[0]+a[1],a[0]+a[1]+a[2]):
            arr[i] = 2
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends