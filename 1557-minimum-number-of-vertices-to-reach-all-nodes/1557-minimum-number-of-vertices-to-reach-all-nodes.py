class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        al = [[] for _ in range(n)]
        
        for i in edges:
            al[i[1]].append(i[0])
        ans = []
        for i in range(len(al)):
            if len(al[i]) ==0:
                ans.append(i)
        return ans