class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = 0

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
            
        while self.s1:
            t = self.s1.pop()
            self.s2.append(t)
            
        self.s1.append(x)
        
        while self.s2:
            t = self.s2.pop()
            self.s1.append(t)
        
    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        ans = self.s1.pop()
        self.s1.append(ans)
        return ans

    def empty(self) -> bool:
       
        return not self.s1 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()