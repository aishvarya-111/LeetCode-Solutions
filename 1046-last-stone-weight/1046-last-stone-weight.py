class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapify(stones)
        while len(stones)>1:
            first = heappop(stones)*-1
            second = heappop(stones)*-1
            if first>second:
                heappush(stones,(first-second)*-1)
        if len(stones)==0:
            heappush(stones,0)
        return abs(stones[0])