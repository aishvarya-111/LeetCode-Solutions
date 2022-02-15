from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        l = digits[-1]*100+digits[-2]*10+digits[-3]
        d = Counter(digits)   
        a =[]
        for i in range(100,l+1,2):
            s = [int(i) for i in str(i)]
            f = Counter(s)
            c =0
            for j,k in f.items():
                if j in d and d[j]>=k:
                    c+=1
            if c==len(f):
                a.append(i)
        return a
                    
            
            
            