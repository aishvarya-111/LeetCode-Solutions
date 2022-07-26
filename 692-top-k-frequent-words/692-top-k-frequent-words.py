class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        
        for i in words:
            d[i]+=1
            
        t = heapq.nsmallest(k,d.items(),key = lambda x:[-x[1],x[0]])
        ans = []
        for i in t:
            ans.append(i[0])
        return ans