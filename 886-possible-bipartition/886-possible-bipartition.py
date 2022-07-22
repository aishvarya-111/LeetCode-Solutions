class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(src,graph,color):
            q = []
            q.append(src)
            color[src]=1
            while(q):
                node = q.pop(0)
                for it in graph[node]:
                    if color[it]==-1:
                        color[it] = 1-color[node]
                        q.append(it)
                    elif color[it]==color[node]:
                        return False
            return True
        
        graph = [[] for _ in range(n+1)]
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

      
        color = [-1]*(n+1)
        
        for i in range(1,len(graph)):
            if color[i]==-1:
                if not dfs(i,graph,color):
                    return False
        return True
        