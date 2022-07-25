class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list) # undirected graph
        edgeSet = set() # all orginal connection
        for connection in connections:
            u, v = connection
            graph[u].append(v)
            graph[v].append(u)
            edgeSet.add((u, v))

        # BFS from 0
        queue = [0]
        visisted = set()
        visisted.add(0)
        addedEdges = 0
        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                if v not in visisted:
                    visisted.add(v)
                    queue.append(v)
                    if (v, u) not in edgeSet: # there is no edge from v to u originally
                        addedEdges += 1
        return addedEdges