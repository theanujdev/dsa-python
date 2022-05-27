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

    def remove(self, data):
        if self.root == None:  # Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node != None:  # Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:  # Match is found. Different cases to be checked
                # Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                # Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                # Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:  # Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                # Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left != None:  # Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data  # The value to be replaced is copied
                    if del_node == del_node_parent:  # If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right == None:  # If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"


tree = BST()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
print(tree)
print(tree.search(12))
print(tree.search(15))
tree.remove(15)
# print(tree)
print(tree)
