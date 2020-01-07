import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):

        # Why is our DLL a good choice to store our elements?
        # Because the DLL has O(1) when it comes to adding or removing the head or the tail.
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.__len__()
