from linkedlist import LinkedList
from linkedlist import Node
# find middle node: (Floyd Cycle Determination)
def find_middle(ll):
    slow = ll.head
    fast=ll.head
    while (fast is not None and fast.next is not None):
        slow= slow.next
        fast = fast.next.next
    return slow.value

#check for loop in the ll. (Floyd Cycle Determination)
def has_loop(ll):
    slow = ll.head
    fast=ll.head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast= fast.next.next
        if slow == fast:
         return True
    return False

#Finding the kth node from the end:
def kth_node_from_end(ll, index):
    if index <= 0 or index > ll.length:
        print("Out of bounds error")
        return None

    slow = ll.head
    fast = ll.head

    for _ in range(index-1):
        if fast is None:
           return None
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    return slow.value

# def remove_duplicated(ll):

def binary_to_decimal(ll):
 num = 0
 current = ll.head
 while current:
    num = num * 2 + current.value
    current = current.next
 return num
   


#partition the list such that anything below "partition_value" is on one side and anything greater than or equal to "partition_value" is in the other side.
def partition_list(ll, partition_value):
   #My approach:
   dummy_list1 = LinkedList(999)
   dummy_list2 = LinkedList(111)
   temp = ll.head
   while temp is not None:
      if temp.value < partition_value:
         dummy_list1.append(temp.value)
      else:
         dummy_list2.append(temp.value)
      temp = temp.next
   
   dummy_list1.tail.next = dummy_list2.head.next
   ll.head = dummy_list1.head.next
#    solution ko approach:
#         if not self.head:
#             return None
    
#         dummy1 = Node(0)
#         dummy2 = Node(0)
#         prev1 = dummy1
#         prev2 = dummy2
#         current = self.head
    
#         while current:
#             if current.value < x:
#                 prev1.next = current
#                 prev1 = current
#             else:
#                 prev2.next = current
#                 prev2 = current
#             current = current.next
    
#         prev1.next = dummy2.next
#         prev2.next = None
    
#         self.head = dummy1.next






# def swap_node_in_pairs(ll):
#    slow = ll.head
#    fast = ll.head   





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3) #3
my_linked_list.append(4) #2
my_linked_list.append(5) #1
# Find middle node
# print("middle node:" , find_middle(my_linked_list))
# Has loop:
# print("Has loop:", has_loop(my_linked_list))
# Kth node from tail:
# print("Has 3rd from tail", kth_node_from_end(my_linked_list,3).value)
