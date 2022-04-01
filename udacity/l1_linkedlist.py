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


"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


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
#     def get_position(self, position):
#         counter = 1
#         current = self.head
#         if position < 1:
#             return None
#         while current:
#             if counter == position:
#                 return current
#             current = current.next
#             counter += 1
#         return None
#
#     def insert(self, new_element, position):
#         counter = 1
#         current = self.head
#         if position > 1:
#             while current and counter < position:
#                 if counter == position - 1:
#                     new_element.next = current.next
#                     current.next = new_element
#                 current = current.next
#                 counter += 1
#         elif position == 1:
#             new_element.next = self.head
#             self.head = new_element
#
#     def delete(self, value):
#         current = self.head
#         previous = None
#         while current.value != value and current.next:
#             previous = current
#             current = current.next
#         if current.value == value:
#             if previous:
#                 previous.next = current.next
#             else:
#                 self.head = current.next
#
#
# # Test cases
# # Set up some Elements
# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)
#
# # Start setting up a LinkedList
# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)
#
# # Test get_position
# # Should print 3
# print(ll.head.next.next.value)
# # Should also print 3
# print(ll.get_position(3).value)
#
# # Test insert
# ll.insert(e4, 3)
# # Should print 4 now
# print(ll.get_position(3).value)
#
# # Test delete
# ll.delete(1)
# # Should print 2 now
# print(ll.get_position(1).value)
# # Should print 4 now
# print(ll.get_position(2).value)
# # Should print 3 now
# print(ll.get_position(3).value)


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            current = new_element

    def show_linkedlist(self):
        current = self.head
        while current:
            print(f'{current.value} -> ', end=" ")
            current = current.next
        print("None")

    def get_position(self, position):
        current = self.head
        pos = 1
        if position < 1:
            return None
        while current:
            if pos == position:
                return current
            current = current.next
            pos += 1
        return None

    def insert(self, new_element, position):
        pos = 1
        current = self.head
        if position > 1:
            while current and pos < position:
                if pos == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                pos += 1
                current = current.next
        elif position == 1:
            new_element.next = current.next
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def pop_last(self):
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next

        if previous:
            previous.next = None
            return current
        else:
            return current


e1 = Element(1)
e2 = Element(20)
e3 = Element(31)
e4 = Element(44)
e5 = Element(101)

l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)

l1.show_linkedlist()
print(l1.get_position(2).value)

l1.insert(e5, 2)
l1.show_linkedlist()

l1.delete(101)
l1.show_linkedlist()

l1.pop_last()
l1.show_linkedlist()
