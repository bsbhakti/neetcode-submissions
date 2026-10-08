class MinStack:

    def __init__(self):
        self.arr = []
        self.stack = []
        self.length = 0
        

    def push(self, value: int) -> None:
        if self.length == 0:
            self.stack.append(value)
            self.arr.append((value,0))
            self.length +=1
        else:
            self.stack.append(value)
            if self.arr[-1][0] > value:
                self.arr.append((value,self.length+1))
            self.length +=1
        #print("push", self.stack, self.arr)

    def pop(self) -> None:
        if self.arr[-1][1] == self.length:
            self.arr.pop()
        self.stack.pop()
        self.length -=1
        #print("pop", self.stack, self.arr)

    

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.length >0:
            return self.arr[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()