class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = [ord(i) - ord('a') for i in s1]
        b = [ord(i) - ord('a') for i in s2]
        ans = [0]*26
        for i in a:
            ans[i]+=1 
        win = [0]*26
        for i in range(len(b)):
            win[b[i]] +=1 
            if i>=len(a):
                win[b[i-len(a)]]-=1
            if win==ans:
                return True
        return False