"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length +=1

    def remove_from_head(self):
        if self.__len__() is 0:
            return None
        head = self.head
        self.delete(self.head)
        return head.value

    def add_to_tail(self, value):
        node = ListNode(value)
        if not self.tail:
            self.head = self.tail = node
        else:   
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1


    def remove_from_tail(self):
        if not self.tail:
            return None
        tail = self.tail
        self.delete(self.tail)
        return tail.value
        

    def move_to_front(self, node):
        if node is self.head:
            return
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
            self.add_to_head(node.value)
        else:
            node.delete()
            self.add_to_head(node.value)
        self.length -= 1

    def move_to_end(self, node):
        if node is self.tail:
            return 
        elif node is self.head:
            self.head = self.head.next
            node.delete()
            self.add_to_tail(node.value)
        else:
            node.delete()
            self.add_to_tail(node.value)
        self.length -= 1

    def delete(self, node):
        self.length -= 1
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        elif node == self.head:
            self.head = node.next
            node.delete()
        elif node == self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        if self.__len__() is 0:
            return None
        current = self.head
        max_val = current.value
        while current:
            max_val = max(max_val, current.value)
            current = current.next
        return max_val
