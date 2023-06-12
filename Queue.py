class QueueList:
    def __init__(self, max_size):
        self.q = []
        self.max_size = max_size
    
    def enqueue(self, x):
        if len(self.q) == self.max_size:
            print("Queue is full")
        else:
            self.q.append(x)
    
    def dequeue(self):
        if len(self.q):
            self.q.pop(0)
        else:
            print("Queue is empty")
    
    def display(self):
        print(self.q)

from queue import Queue

class QUEUE:
    def __init__(self,max_size):
        self.q = Queue(maxsize=max_size)
    
    def enqueue(self, x):
        self.q.put_nowait(x)
    
    def dequeue(self):
        print(self.q.get_nowait())
    
    def isempty(self):
        return self.q.empty()
    
    def isfull(self):
        self.q.full()
    
    def display(self):
        print(self.q)

if __name__ == "__main__":
    queue = QUEUE(5)
    while True:
        print("Enter 1. Add 2. Remove 3. Show 4. Exit")
        opt = int(input("Enter Option: "))
        if opt == 1:
            x = int(input("Enter the element: "))
            queue.enqueue(x)
        elif opt == 2:
            queue.dequeue()
        elif opt == 3:
            queue.display()
        elif opt == 4:
            break
        else:
            print("Unsupported Option")