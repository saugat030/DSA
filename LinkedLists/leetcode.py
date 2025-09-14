from linkedlist import LinkedList


# find middle node:
def find_middle(ll):
    slow = ll.head
    fast=ll.head
    while (fast is not None and fast.next is not None):
        slow= slow.next
        fast = fast.next.next
    return slow.value

def has_loop(ll):
    slow = ll.head
    fast=ll.head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast= fast.next.next
        if slow == fast:
         return True
    return False


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
# Find middle node
# print("middle node:" , find_middle(my_linked_list))
print("Has loop:", has_loop(my_linked_list))