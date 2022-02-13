class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d1,d2 = {},{}
        for i in range(len(nums)):
            if(i%2==0):
                if nums[i] in d1:
                    d1[nums[i]]+=1
                else:
                    d1[nums[i]]=1
            else:
                if nums[i] in d2:
                    d2[nums[i]]+=1
                else:
                    d2[nums[i]]=1
        s1 = sum(d1.values())
        s2 = sum(d2.values())
        
        h1 = [(d1[k],k) for k in d1.keys()]
        h2 = [(d2[k],k) for k in d2.keys()]
        h1.sort(reverse=True)
        h2.sort(reverse=True)
        print(h1,h2)
        for i in h1:
            for j in h2:
                if i[1]!=j[1]:
                    return s1-i[0]+s2-j[0]
                
        return min(s1,s2)