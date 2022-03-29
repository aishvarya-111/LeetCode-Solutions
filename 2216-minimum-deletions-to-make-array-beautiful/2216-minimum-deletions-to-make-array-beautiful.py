class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = []
        c=0
        for i in nums:
            if len(ans)%2!=0 and ans[-1]==i:
                c+=1
            else:
                ans.append(i)
        if len(ans)%2!=0:
            c=c+1
        return c