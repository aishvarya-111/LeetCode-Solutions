class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.title()
        
        l = list(title.split())
        for i in range(len(l)):
            if(len(l[i])<3):
                l[i] = l[i].lower()
        s = " "
        s=s.join(l)
        return s