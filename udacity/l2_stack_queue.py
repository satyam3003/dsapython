# class Element(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList(object):
#     def __init__(self, head=None):
#         self.head = head
#
#     def append(self, new_element):
#         current = self.head
#         if self.head:
#             while current.next:
#                 current = current.next
#             current.next = new_element
#         else:
#             self.head = new_element
#
#     def insert_first(self, new_element):
#         new_element.next = self.head
#         self.head = new_element
#
#     def delete_first(self):
#         if self.head:
#             deleted_element = self.head
#             temp = deleted_element.next
#             self.head = temp
#             return deleted_element
#         else:
#             return None
#
#
# class Stack(object):
#     def __init__(self, top=None):
#         self.ll = LinkedList(top)
#
#     def push(self, new_element):
#         self.ll.insert_first(new_element)
#
#     def pop(self):
#         return self.ll.delete_first()


"""  -----------------Stack-------------------- """

print("Stackkk.....")
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def showlist(self):
        current = self.head
        while current:
            print(f"{current.value} ->", end=" ")
            current = current.next
        print("")

    def insert_first(self, insert_element):
        insert_element.next = self.head
        self.head = insert_element

    def remove_first(self):
        current = self.head
        if self.head:
            self.head = current.next
            return current
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.stack_list = LinkedList(top)

    def push(self, element):
        self.stack_list.insert_first(element)

    def pop(self):
        return self.stack_list.remove_first()

    def show(self):
        self.stack_list.showlist()


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
stack.push(e4)
stack.show()

print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
stack.show()

stack.push(e4)
stack.push(e3)
stack.show()
print(stack.pop().value)
stack.show()


print("'Queue......")
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
