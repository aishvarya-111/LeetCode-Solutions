class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        #method 1
        #z = list(zip(*items))
        #if ruleKey == "type":
        #    return z[0].count(ruleValue)
        #elif ruleKey == "color":
        #    return z[1].count(ruleValue)
        #else:
        #    return z[2].count(ruleValue)
        
        #method 2
        res=0
        for i in items:
            if(ruleKey=='color' and i[1]==ruleValue):
                res+=1
            elif(ruleKey=='type' and i[0]==ruleValue):
                res+=1
            elif(ruleKey=='name' and i[2]==ruleValue):
                res+=1
        return res