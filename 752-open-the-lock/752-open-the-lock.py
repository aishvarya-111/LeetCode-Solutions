class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited:
            return -1
        q1 = set(['0000'])
        q2 = set([target])
        step = 0
        
        # helper to dial up
        def up(num,j):
            lst = list(num)
            if num[j] == '9':
                lst[j] = '0'
            else: 
                lst[j] = str(int(num[j]) + 1)
            return ''.join(lst)
        
        # helper to dial down
        def down(num,j):
            lst = list(num)
            if num[j] == '0':
                lst[j] = '9'
            else: 
                lst[j] = str(int(num[j]) - 1)
            return ''.join(lst)
        
        while q1 and q2:
            tmp = set()
           
            for cur in q1:
                if cur in visited: continue
                # Overlap exists
                if cur in q2: return step
                visited.add(cur)
                
                for j in range(4):
                    up_num = up(cur, j)
                    if up_num not in visited: 
                        tmp.add(up_num)
         
                    down_num = down(cur, j)
                    if down_num not in visited: 
                        tmp.add(down_num)

            step += 1
            q1 = q2
            q2 = tmp
            
        return -1