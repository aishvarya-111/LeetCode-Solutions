class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_pro = 0
        mn_sell = prices[0]
        for i in prices[1:]:
            mn_sell = min(mn_sell,i)
            mx_pro = max(mx_pro,i-mn_sell)
            
        return mx_pro