class MinStack:

    def __init__(self):
        self.stack = [] # normal stack for elements
        self.min_stack = [] # stack for holding min value at end

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if min_stack exists, then compare end value with append value and add the min of it to guarantee that min_stack's end is smallest
        if self.min_stack:
            self.min_stack.append(min(val,self.min_stack[-1]))
        else:
            self.min_stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# time: O(1) amortized, space: O(n)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin()) # return -3
obj.pop()
print(obj.top()) # return 0
print(obj.getMin()) # return -2
