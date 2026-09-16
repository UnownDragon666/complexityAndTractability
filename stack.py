# Last in first out
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data: str):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


x = Stack()

x.push("s")

print(x.peek())
