class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #i=0
        #while(i<len(s)):
         #   if s[i]=='#':
          #      s = s.replace(s[-1],"",1)
           # else:
            #    i+=1
        #j = 0        
        #while(j<len(t)):
         #   if t[i]=='#':
          #      b = b[:-1]
           # else:
            #    b+=t[i]
        #return True if(a==b) else False
        
        d = []
        i = 0
        while(i<len(s)):
            if s[i]!='#':
                d+=s[i]
            elif d:
                d.pop()
            i+=1 
        
        h = []
        i = 0
        while(i<len(t)):
            if t[i]!='#':
                h+=t[i]
            elif h:
                h.pop()
            i+=1  
        return True if(d==h) else False
    