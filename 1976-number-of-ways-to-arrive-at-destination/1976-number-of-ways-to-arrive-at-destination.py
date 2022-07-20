class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        al = [[] for i in range(n)]
        
        for i in roads:
            a,b,w=i[0],i[1],i[2]
            al[a].append([b,w])
            al[b].append([a,w])
       
        d = [float('inf')]*n
        ways = [0]*n
        pri = []
        heapify(pri)
        heappush(pri,[0,0])
        d[0] = 0
        ways[0] = 1
        while pri:
            node = heappop(pri)
            dis = node[0]
            ele = node[1]
            
            if d[ele]<dis:
                continue 
                
            for i in al[ele]:
                nxt = i[0]
                dist = i[1]
                if dis+dist<d[nxt]:
                    ways[nxt] = ways[ele]
                    d[nxt] = d[ele] + dist
                    heappush(pri,[d[nxt],nxt])
                    
                elif dis + dist == d[nxt]:
                    ways[nxt] = (ways[ele]+ways[nxt])%(10**9 + 7)
       
        return ways[n-1]