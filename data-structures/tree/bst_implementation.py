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
        if self.root is None:  # Tree is empty
            return "Tree is empty"
    
        current_node = self.root
        parent_node = None

        while current_node is not None:  # Traverse the tree
            if current_node.data > data:  # Go left
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:  # Go right
                parent_node = current_node
                current_node = current_node.right
            else:  # Node found
                # Case 1: Node has no children (leaf node)
                if current_node.left is None and current_node.right is None:
                    if parent_node is None:  # Node is root
                        self.root = None
                    elif parent_node.data > current_node.data:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return
                
                # Case 2: Node has only a left child
                elif current_node.right is None:
                    if parent_node is None:  # Removing root
                        self.root = current_node.left
                    elif parent_node.data > current_node.data:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right = current_node.left
                    return
                
                # Case 3: Node has only a right child
                elif current_node.left is None:
                    if parent_node is None:  # Removing root
                        self.root = current_node.right
                    elif parent_node.data > current_node.data:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right
                    return               
                
                # Case 4: Node has two children
                else:
                    # Find the in-order successor (leftmost node in the right subtree)
                    successor_parent = current_node
                    successor = current_node.right
                    while successor.left:  # Traverse left to find the smallest value
                        successor_parent = successor
                        successor = successor.left
                    
                    # Replace the data of the node to be deleted with the successor's data
                    current_node.data = successor.data

                    # Remove the successor node from its original position
                    if successor_parent == current_node:  # Successor is the direct right child
                        successor_parent.right = successor.right
                    else:  # Successor has no left child but may have a right child
                        successor_parent.left = successor.right
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
