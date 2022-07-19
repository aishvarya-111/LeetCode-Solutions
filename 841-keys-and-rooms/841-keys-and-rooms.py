class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        n = len(rooms)
        v = [0]*len(rooms)
        q = []
        q.append(0)
        while(q):
            node = q.pop(0)
            v[node]=1
            for i in rooms[node]:
                if v[i]==0:
                    q.append(i)
                    v[i]=1 
                
        if sum(v) == len(rooms):
            return True
        return False