class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
     #Print all the values of the stack   
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push_to_stack(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop_from_stack(self):
        if self.height == 0:
            print("No items on stack to pop")
            return None
        else:
         temp = self.top
         self.top = self.top.next
         temp.next = None
        self.height -= 1
        return temp
        

stack = Stack(1)