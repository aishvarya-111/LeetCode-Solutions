#User function Template for python3
class Solution:
	def countTriplet(self, a, n):
	    c = 0
	    m = max(a)
		d = [0]*(m+1)
		a.sort()
		for i in range(n):
		    d[a[i]]+=1
		
		for i in range(n):
		    for j in range(i+1,n):
		        t = a[i] + a[j]
		        if(t<=m and d[t]>0):
		            c+=1
		return c
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends