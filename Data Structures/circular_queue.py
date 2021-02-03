class Circular:
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1
    
    def enqueue(self,data):
        if ((self.rear + 1) % self.k == self.front):
            print("The circular queue is full\n")

        else:
            
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data
        if self.front == -1:
            self.front = 0
    
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear == self.front:
            temp = self.queue[self.front]
            self.rear = -1
            self.front = -1
            return temp
        else:
            temp = self.queue.pop(self.front)
            self.front = (self.front + 1) % self.k
            return temp


    def display(self):
        if self.front == -1:
            print("Empty queue")
        elif self.rear > self.front:
            for i in range(self.front,self.rear+1):
                print(i, end = " ")
            print()
        
        
obj = Circular(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.display()
obj.dequeue()
print("After removing an element from the queue")
obj.display()