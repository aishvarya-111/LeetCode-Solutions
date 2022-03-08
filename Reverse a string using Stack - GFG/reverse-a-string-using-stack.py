#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    
    #Add code here
    d = []
    for i in S:
        d.append(i)
    s=""
    for i in range(len(d)):
        s=s+d.pop()
    return s

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends