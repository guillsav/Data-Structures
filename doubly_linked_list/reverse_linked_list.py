from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

""" 
Given a linkedlist reverse the order of the nodes without the use of recursion, (you may not store the list in a none list data-structure).

Input: 1->2->3
Ouput: 3->2->1

3 -> 2 -> 
"""

def reverse_linked_list(head):
    prev = ListNode()

    while head:
      next_node = ListNode(head.next)
      head.next = prev
      prev = head
      head = next_node
    
    return prev



  
    # while current:
    #   prev = next_node.next
    #   prev.next = current
    #   next_node = prev.next
    #   current = next_node.next
    #   return prev


my_list = DoublyLinkedList()
my_list.add_to_tail(1)
my_list.add_to_tail(2)
my_list.add_to_tail(3)
my_list.add_to_tail(4)

print(reverse_linked_list(my_list.head))



