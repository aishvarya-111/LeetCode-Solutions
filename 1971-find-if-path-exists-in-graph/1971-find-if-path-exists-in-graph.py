class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        al = [[] for i in range(n)]
        for i in range(len(edges)):
            al[edges[i][0]].append(edges[i][1])
            al[edges[i][1]].append(edges[i][0])
        v = [0]*n 
        q = []
        q.append(source)
        v[source] = 1
        while q:
            node = q.pop(0)
            if node == destination:
                return True
            for i in al[node]:
                if v[i]==0:
                    q.append(i)
                    v[i] = 1 
        
        if v[source] == 0 or v[destination] == 0:
            return False
        else:
            return True
                
        
        