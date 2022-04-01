# list based stack
print("List based stack")


class Stack:
    def __init__(self):
        self.list_stack = list()

    def isEmpty(self):
        return len(self.list_stack) == 0
        # return len(self.list_stack) == 0

    def __len__(self):
        return len(self.list_stack)

    def push(self, value):
        self.list_stack.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.list_stack.pop()

    def peep(self):
        if not self.isEmpty():
            return self.list_stack[-1]

    def view(self):
        return self.list_stack


s1 = Stack()
s1.push(5)
s1.push(6)
s1.push(8)
s1.push(11)

print(s1.pop())
print(s1.peep())
print(s1.view())


# linked list based stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LLStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def isEmpty(self):
        return self.count == 0

    def pop(self):
        if not self.isEmpty():
            current = self.top
            self.top = current.next
            self.count -= 1
            return current.value

    def __len__(self):
        return self.count

    def peep(self):
        if not self.isEmpty():
            return self.top.value

    def view(self):
        current = self.top
        while current is not None:
            print(f"{current.value}", end="<-")
            current = current.next
        print("End")


print("\nLinked list stack")
s2 = LLStack()
print(s2.isEmpty())
s2.push(4)
s2.push(5)
s2.push(25)
s2.push(101)
print(len(s2))
print(s2.pop())
s2.view()
print(len(s2))