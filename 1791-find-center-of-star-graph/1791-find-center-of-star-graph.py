class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = 0
        for i in edges:
            n = max(n,max(i))
        al = [[] for i in range(n+1)]
        
        for i in range(len(edges)):
            al[edges[i][0]].append(edges[i][1])
            al[edges[i][1]].append(edges[i][0])
           
        for i in range(n+1):
            if len(al[i])==n-1:
                ans = i 
                break
        return ans
        