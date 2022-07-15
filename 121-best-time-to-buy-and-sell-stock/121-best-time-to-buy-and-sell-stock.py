class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_pro = 0
        l,r = 0,0 
        while(l<len(prices) and r<len(prices)):
            pro = prices[r] - prices[l]
            if prices[l]>prices[r]:
                l = r
            else:
                mx_pro = max(mx_pro,pro)
            r+=1
        return mx_pro