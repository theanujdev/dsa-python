class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self) -> str:
        return str(vars(self))

    def peek(self):
        return self.top['data']

    def push(self, data):
        new_node = {
            "data": data,
            "next": None
        }
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node['next'] = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 1:
            self.bottom = None

        if self.length == 0:
            print("Empty stack!")
            return
        cn = self.top
        self.top = self.top['next']
        self.length -= 1
        return cn['data']

    def is_empty(self):
        return self.length == 0


s = Stack()
s.push(2)
s.push(6)
s.push(12)
# print(s.pop())
# print(s.pop())
print(s.pop())
print(s.peek())
print(s)
