from collections import deque

queue=[]
queue.insert(0,2)
queue.insert(0,5)
queue.insert(0,10)
print(queue)

print(queue.pop())
print(queue.pop())
print(queue.pop())
# print(queue.pop())

q=deque()
q.appendleft(5)
q.appendleft(55)
q.pop()
print(q)