""" 
Given a linkedlist find the middle node using one loop pass
Input: 0->1->2->3->4->5->6->7->8->9->10->None
Ouput: 6
"""

from doubly_linked_list import DoublyLinkedList

# Create the linkedlist.
my_list = DoublyLinkedList()
my_list.add_to_tail(0)
my_list.add_to_tail(1)
my_list.add_to_tail(2)
my_list.add_to_tail(3)
my_list.add_to_tail(4)
my_list.add_to_tail(5)
my_list.add_to_tail(6)
my_list.add_to_tail(7)
my_list.add_to_tail(8)
my_list.add_to_tail(9)
my_list.add_to_tail(10)

def tortoise_and_the_hare(list: DoublyLinkedList) -> int:
    # Define 2 pointers pointing at the head of the list.
    # The slow_node will iterate through the list 1 node at the time.
    # The fast_node will iterate through the list 2 nodes at the time.
    slow_node = fast_node = list.head

    # Loop through the list as long while the fast_node is not None.
    while fast_node:
        # Iterate through the list 1 node at the time.
        slow_node = slow_node.next
        # If the fast_node is None break out of the while loop.
        if not fast_node.next:
            break
        # else iterate through the list 2 nodes at the time.
        fast_node = fast_node.next.next

    # if the fast_node is None return the slow_node.
    return slow_node

print(tortoise_and_the_hare(my_list))



