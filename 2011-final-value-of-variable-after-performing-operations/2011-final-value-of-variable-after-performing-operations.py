class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        r = 0
        for i in operations:
            if i == '--X' or i =='X--':
                r-=1
            else:
                r+=1
        return r