
# class Queue:
#     def __init__(self,queue = None):
#         if queue is None:
#             self.queue = []
#         else:
#             self.queue = queue
#     def __repr__(self):
#         return str(self.queue)
#     def append(self,value):#enqueue
#         self.queue.append(value)
#         return self.queue
#     def pop(self):#dequeue
#         try:
#             return self.queue.pop(0)
#         except IndexError as e:
#             return e
#     def isFull(self):
#         if len(self.queue) > 0:
#             return True
#         return False
#     def isEmpty(self):
#         if len(self.queue) == 0:
#             return True
#         return False
        
# queue = Queue()

from collections import deque
# Enqueuing
data = deque()
data.append(2)
data.append(3)

# Dequeuing
element = data.popleft()
print(element, data)
