class MinStack:

    def __init__(self):
        self.vals = []

    def push(self, val: int) -> None:
        if len(self.vals)>0:
            last_value = self.vals[-1][-1]
            if val<last_value:
                self.vals.append([val,val])
            else:
                self.vals.append([val,last_value])
        else:
            self.vals.append([val,val])

    def pop(self) -> None:
        self.vals.pop()

    def top(self) -> int:
        return self.vals[-1][0]

    def getMin(self) -> int:
        return self.vals[-1][-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
param_4 = obj.getMin()