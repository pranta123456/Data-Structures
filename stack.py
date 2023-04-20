# Using List
class StackList:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

#Using Modules
import queue
class Stack:
    def __init__(self):
        self.stack = queue.LifoQueue()
    
    def push(self, element):
        self.stack.put(element, timeout=1)
    
    def pop(self):
        if self.stack:
            print(self.stack.get(timeout=1))
    
    def peek(self):
        if self.stack:
            return self.stack.queue[-1]


if __name__ == '__main__':
    stack = Stack()
    print("Pushing in a stack")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.stack.queue)
    print("Popping in a stack")
    stack.pop()
    print(stack.stack.queue)
    print("Peek element")
    print(stack.peek())
