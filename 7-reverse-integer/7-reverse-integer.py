class Solution:
    def reverse(self, x: int) -> int:
        #Reversing using Slicing in python
        s = str(x)
        if(x<0):
            s=s[::-1] #Reversing the string
            s = s[:-1] #Removing the '-' sign
            x = int(s)
            x=-x
        else:
            s=s[::-1]
            x = int(s)   
        a = pow(2,31)
        if(x<(-a) or x>(a-1)): #Check the range
            return 0
        else:
            return(x)