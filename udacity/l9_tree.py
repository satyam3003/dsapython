class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start):
        if start:
            return [start.value] + self.preorder_print(start.left) + self.preorder_print(start.right)
        else:
            return []

n1 = Node(4)
n2 = Node(5)
n3 = Node(6)

bt = BinaryTree(n2)
bt.root.left = n1
bt.root.right = n3

print(bt.preorder_print(n2))
