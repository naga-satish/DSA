from DoublyLinkedList import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, item):
        self.queue.insert(item)

    def dequeue(self):
        temp = self.queue.get_tail()
        self.queue.delete_tail()
        return temp

    def isEmpty(self):
        return self.queue.length == 0


if __name__ == '__main__':
    some_queue = Queue()
    print(some_queue.isEmpty())
    for i in range(1):
        some_queue.enqueue(i**i)

    print(some_queue.dequeue())
    print(some_queue.dequeue())

