class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        
        """
        v = [0]*len(rooms)
        def dfs(node):
            if v[node]==0:
                v[node]=1
                
            for i in rooms[node]:
                if v[i]==0:
                    v[i]=1
                    dfs(i)
                    
        dfs(0)
        return sum(v)==len(rooms)
        