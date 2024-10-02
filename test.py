import queue
q = queue.Queue()

test = [1,2,3]

print(test.pop(0))
test = "asdf"
for i in range(len(test)-1):
    print(test[i:i+2])