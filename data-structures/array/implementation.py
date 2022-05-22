class Array():
    def __init__(self) -> None:
        self.length = 0
        self.data = {}

    def get(self, index: int):
        return self.data[index]

    def append(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        del self.data[self.length-1]
        self.length -= 1

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[index] = self.data[index+1]
        del self.data[self.length-1]
        self.length -= 1

    def __str__(self):
        # print(self.data.values())
        return str(vars(self))


arr = Array()
arr.append(34)
arr.append("#@")
arr.pop()
arr.append("214")
arr.delete(1)
arr.append("ad")
print(arr.get(1))
# print(vars(arr))
print(arr)
