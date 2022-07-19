class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
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
        
        color = [-1]*(len(graph))
        
        for i in range(len(graph)):
            if color[i]==-1:
                if not dfs(i,graph,color):
                    return False
        return True
        