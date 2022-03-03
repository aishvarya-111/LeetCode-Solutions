#User function Template for python3

class Solution:
    def endPoints(self, matrix, m, n):
        ##code here
        i,j=0,0
        d = 'r'
        while(i<m and j<n and i>=0 and j>=0):
            if matrix[i][j] == 0 and d=='r':
                j+=1 
            elif matrix[i][j] == 0 and d=='l':
                j-=1 
            elif matrix[i][j] == 0 and d=='u':
                i-=1 
            elif matrix[i][j] == 0 and d=='d':
                i+=1 
            elif matrix[i][j] == 1 and d=='u':
                matrix[i][j]=0
                j+=1
                d = 'r'
            elif matrix[i][j] == 1 and d=='r':
                matrix[i][j]=0
                i+=1
                d = 'd'
            elif matrix[i][j] == 1 and d=='d':
                matrix[i][j]=0
                j-=1
                d = 'l'
            elif matrix[i][j] == 1 and d=='l':
                matrix[i][j]=0
                i-=1
                d = 'u'
        
        if i>=m:
            i-=1 
        if j>=n:
            j-=1
        if i<0:
            i=0
        if j<0:
            j=0
        
        return [i,j]
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends