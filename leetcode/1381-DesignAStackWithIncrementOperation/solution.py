class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) != self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.stack))):
            self.stack[i] += val

# Time: O(n)
# Memory: O(n)

stk = CustomStack(3)
stk.push(1)                         # stack becomes [1]
stk.push(2)                          # stack becomes [1, 2]
print("Expected: [1,2], Actual: ", stk.stack)
stk.pop()                            # return 2 --> Return top of the stack 2, stack becomes [1]
print("Expected: [1], Actual: ", stk.stack)
stk.push(2)                          # stack becomes [1, 2]
stk.push(3)                          # stack becomes [1, 2, 3]
stk.push(4)                          # stack still [1, 2, 3], Do not add another elements as size is 4
print("Expected: [1,2,3], Actual: ", stk.stack)
stk.increment(5, 100)                # stack becomes [101, 102, 103]
stk.increment(2, 100)                # stack becomes [201, 202, 103]
print("Expected: [201,202,103], Actual: ", stk.stack)
stk.pop()                            # return 103 --> Return top of the stack 103, stack becomes [201, 202]
stk.pop()                            # return 202 --> Return top of the stack 202, stack becomes [201]
stk.pop()                            # return 201 --> Return top of the stack 201, stack becomes []
stk.pop()                            # return -1 --> Stack is empty return -1.
print("Expected: [], Actual: ", stk.stack)