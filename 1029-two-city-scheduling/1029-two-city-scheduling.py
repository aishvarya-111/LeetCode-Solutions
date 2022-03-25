class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0]-x[1])
        ca = 0
        cb = 0
        for i in costs[:len(costs)//2]:
            ca+=i[0]
        for i in costs[len(costs)//2:]:
            cb+=i[1]
        return ca+cb