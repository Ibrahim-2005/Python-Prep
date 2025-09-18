from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
    
    def enqueue(self,val):
        self.queue.appendleft(val)
    
    def dequeue(self):
        return self.queue.pop()
    def is_empty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)