import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because the DLL has O(1) when it comes to adding or removing the head or the tail.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.len() is 0:
            return
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
