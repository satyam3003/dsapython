class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        current = self.head
        self.head = current.next
        return current.value

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.value}", end=" ")
            current_node = current_node.next

    def remove(self, target):
        current_node = self.head
        previous_node = None
        while current_node is not None and current_node.value != target:
            previous_node = current_node
            current_node = current_node.next

        if current_node:
            if current_node == self.head:
                self.head = current_node.next
            else:
                previous_node.next = current_node.next
        else:
            print("Value doesnt exits.")


ll = LinkedList()
ll.add(5)
ll.add(7)
ll.add(19)
ll.remove(5)
ll.remove(5)
# ll.pop()

ll.traverse()
