class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        state = 1 << n
        queue = deque([(i, state) for i in range(n)])
        cnt = 0
        vis = set()
        while queue:
            l = len(queue)
            for i in range(l):
                cur, state = queue.popleft()
                
                state |= 1 << cur
               
                if state == (1 << (n + 1)) - 1:
                    return cnt
                for nxt in graph[cur]:
                    if (nxt, state) not in vis:
                        queue.append((nxt, state))
                        vis.add((nxt, state))
            cnt += 1