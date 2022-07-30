class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class LinkedList():
    def __init__(self, data) -> None:
        self.head = {
            "data": data,
            "next": None,
            "prev": None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        return str(vars(self))

    def append(self, data):
        new_node = {
            "data": data,
            "next": None,
            "prev": None
        }
        new_node['prev'] = self.tail
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = {
            "data": data,
            "next": None,
            "prev": None
        }
        self.head['prev'] = new_node
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        elif index > self.length:
            self.append(data)
            return

        new_node = {
            "data": data,
            "next": None,
            "prev": None
        }
        node = self.head
        for _ in range(index-1):
            node = node['next']
        node['next']['previous'] = new_node
        new_node['next'] = node['next']
        new_node['prev'] = node
        node['next'] = new_node
        self.length += 1

    def delete(self, index):
        if index == 0:
            self.head = self.head['next']
            self.head['prev'] = None
            self.length -= 1
            return
        elif index >= self.length:
            print("Index exceeded size limit!")
            return

        current_node = self.head
        for _ in range(index-1):
            current_node = current_node['next']
        current_node['next'] = current_node['next']['next']
        self.length -= 1

    def printList(self):
        arr = []
        current_node = self.head
        while(current_node != None):
            arr.append(current_node['data'])
            current_node = current_node['next']
        print(arr)


myLS = LinkedList(23)
myLS.append(34)
myLS.append(21)
myLS.append(25)
myLS.prepend(11)
myLS.insert(3, 55)
myLS.printList()
# myLS.delete(3)
# myLS.printList()
# print(myLS)
# print(myLS.head['next'])
