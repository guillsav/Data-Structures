import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        # Because the DLL has O(1) when it comes to adding or removing the head or the tail.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)


    def dequeue(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.__len__()
