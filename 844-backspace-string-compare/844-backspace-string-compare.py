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
        for i in range(len(s)):
            if s[i]!='#':
                d+=s[i]
            elif d:
                d.pop()
           
        h = []
        for j in range(len(t)):
            if t[j]!='#':
                h+=t[j]
            elif h:
                h.pop()
                
        return d==h
    