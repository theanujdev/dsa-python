class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, data) -> None:
        self.head = {
            "data": data,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        return str(vars(self))

    def append(self, data):
        new_node = {
            "data": data,
            "next": None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = {
            "data": data,
            "next": None
        }
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
            "next": None
        }
        node = self.head
        for _ in range(index-1):
            node = node['next']
        new_node['next'] = node['next']
        node['next'] = new_node
        self.length += 1

    def delete(self, index):
        if index == 0:
            self.head = self.head['next']
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

    def reverse(self):
        cn = self.head
        self.tail = cn
        nn = cn['next']
        while nn:
            temp = nn['next']
            nn['next'] = cn
            cn = nn
            nn = temp
        self.head['next'] = None
        self.head = cn

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
# myLS.prepend(11)
myLS.insert(5, 55)
myLS.printList()
myLS.delete(3)
myLS.printList()
# myLS.reverse()
# myLS.printList()
print(myLS)
# print(myLS.head['next'])
