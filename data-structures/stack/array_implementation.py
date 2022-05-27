class Stack():
    def __init__(self) -> None:
        self.array = []

    def __str__(self) -> str:
        return str(vars(self))

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if len(self.array) < 1:
            print("Empty stack!")
            return
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0


s = Stack()
print(s.is_empty())
s.push(2)
s.push(6)
s.push(12)
# print(s.pop())
# print(s.pop())
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s)
