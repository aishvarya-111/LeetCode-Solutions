class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        al = [[] for i in range(n+1)]
        
        for i in range(len(trust)):
            al[trust[i][0]].append(trust[i][1])
       
        ans = -1
        for i in range(1,len(al)):
            if len(al[i])==0:
                ans = i
                
        if ans!=-1:
            for i in range(1,len(al)):
                if i!=ans and ans not in al[i]:
                    ans = -1
                    break
        return ans