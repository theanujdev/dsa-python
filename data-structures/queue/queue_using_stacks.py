class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self) -> str:
        return str(vars(self))

    def peek(self):
        if len(self.s1) == 0:
            print("Queue empty")
        else:
            return self.s1[len(self.s1)-1]

    def enqueue(self, data):
        for _ in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(data)
        for _ in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)

    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue Empty")
            return
        else:
            return self.s1.pop()


q = Queue()
q.enqueue(2)
q.enqueue(6)
q.enqueue(33)
q.dequeue()

# print(s.pop())
# print(s.pop())
# print(q.pop())
print(q.peek())
# q.dequeue()
# print(q.peek())
print(q)
