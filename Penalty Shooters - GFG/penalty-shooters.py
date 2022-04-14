#User function Template for python3

class Solution:
    
    def goals(self, x,y,z):
        # code here
        g,n=0,0
        while(z!=1):
            if(x%z!=0 and y%z!=0):
                z-=1 
            elif(x%z==0 and y%z==0):
                x-=1
                g+=1
            elif(x%z==0 and y%z!=0):
                x-=1
                g+=1
            elif(y%z==0 and x%z!=0):
                y-=1 
                n+=1
        return [g,n]
                
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X, Y, Z = [int(a) for a in input().split()]

        ob = Solution()
        c1, c2 = ob.goals(X, Y, Z)
        print(c1, end=" ")
        print(c2)
# } Driver Code Ends