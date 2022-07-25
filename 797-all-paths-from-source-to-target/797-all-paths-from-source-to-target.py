class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        res = []

        def dfs(node, temp):
            if node == n:
                temp.append(node)
                res.append(temp.copy())
                return
            
            for neighbor in graph[node]:
                dfs(neighbor, temp + [node])
            return
        
        dfs(0, [])
        return res