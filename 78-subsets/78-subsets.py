class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = pow(2,len(nums))
        a=[[]]
        for i in range(1,n):
            s = bin(i)[2:]
            s=s[::-1]
            print(s)
            h=[]
            for j in range(len(s)):
                if(s[j]=='1'):
                    h.append(nums[j])
            a.append(h)
        return a