import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because the DLL has O(1) when it comes to adding or removing the head or the tail.
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.len() is 0:
            return
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
