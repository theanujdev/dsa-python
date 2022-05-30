class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self) -> None:
        self.root = None

    def __str__(self) -> str:
        return str(vars(self))

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            cn = self.root
            while True:
                if data < cn.data:  # go to left
                    if cn.left is None:
                        cn.left = new_node
                        return
                    cn = cn.left

                elif data > cn.data:  # go to right
                    if cn.right is None:
                        cn.right = new_node
                        return
                    cn = cn.right
                else:
                    return print("Data already exists!")

    def search(self, data):
        if self.root is None:
            return False
        cn = self.root
        while cn:
            if data < cn.data:  # go to left
                cn = cn.left
            elif data > cn.data:  # go to right
                cn = cn.right
            else:
                return data
        return False

    def bfs(self):
        cn = self.root
        result = []
        queue = []
        queue.append(cn)
        while len(queue):
            cn = queue.pop(0)
            result.append(cn.data)
            if cn.left:
                queue.append(cn.left)
            if cn.right:
                queue.append(cn.right)
        return result

    def recursive_bfs(self, queue, result):
        if len(queue) == 0:
            return result
        cn = queue.pop(0)
        result.append(cn.data)
        if cn.left:
            queue.append(cn.left)
        if cn.right:
            queue.append(cn.right)
        return self.recursive_bfs(queue, result)


tree = BST()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# print(tree)
# print(tree.search(12))
# print(tree.search(15))
# print(tree)

#     9
#  4     20
# 1  6  15  170

print(tree)

print(tree.bfs())
print(tree.recursive_bfs([tree.root], []))
# [9,4,20,1,6,15,170]
