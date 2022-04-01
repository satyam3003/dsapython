print("Queue using Python List")


class Queue:
    def __init__(self):
        self.queue_list = list()

    def __len__(self):
        return len(self.queue_list)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, value):
        self.queue_list.append(value)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue_list.pop(0)
        else:
            return -1

    def view(self):
        return self.queue_list

    def peep(self):
        if not self.isEmpty():
            return self.queue_list[0]
        else:
            return -1


q1 = Queue()
q1.enqueue(5)
q1.enqueue(10)
q1.enqueue(15)
q1.enqueue(20)
print(len(q1))
print(q1.isEmpty())
print(q1.dequeue())
print(q1.view())
