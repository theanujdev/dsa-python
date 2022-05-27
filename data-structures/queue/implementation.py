class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self) -> str:
        return str(vars(self))

    def peek(self):
        return self.first['data']

    def enqueue(self, data):
        new_node = {
            "data": data,
            "next": None
        }

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last['next'] = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 1:
            self.last = None

        if self.length == 0:
            print("Empty Queue!")
            return
        cn = self.first
        self.first = self.first['next']
        self.length -= 1
        return cn['data']

    def is_empty(self):
        return self.length == 0


q = Queue()
q.enqueue(2)
q.enqueue(6)
q.enqueue(33)
# q.dequeue()

# print(s.pop())
# print(s.pop())
# print(q.pop())
print(q.peek())
q.dequeue()
print(q.peek())
print(q)
