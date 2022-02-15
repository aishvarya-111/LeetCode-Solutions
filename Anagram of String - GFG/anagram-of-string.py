# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    
    s = str1
    for i in s:
        if i in str2:
            s = s.replace(i,"",1)
            str2 = str2.replace(i,"",1)
    n = len(s)+len(str2)
    return n
    #add code here
    
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends