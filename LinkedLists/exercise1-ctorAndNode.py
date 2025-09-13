class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def displayList(self):
        if self.length == 0:
            print("The list is empty.")
            return
        temp = self.head
        print("Current List:", end=" ")
        while temp is not None:
            print(temp.value, end=" -> " if temp.next else "")
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            print("Pop attempted, but the list is already empty.")
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None  
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        print(f"Popped value: {temp.value}")
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0 or self.length is None:
         print("Linked List khali creating new node.")
         self.head = new_node
         self.tail= new_node
        else:
         temp = self.head
         self.head = new_node
         self.head.next = temp
        #  new_node.next = self.head //This also works
        #  self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
         return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        # This is for if the linked list only has one item. Thats why we check this after the length has been decremented to zero.
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self,index):
        if index <0 or index >= self.length:
            print("Out of bounds error")
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        # Get method already returns the node where the index is at. Error handeling ni sab get mai garisakya xa.
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert(self, index ,value):
        if index < 0 or index > self.length:
         print("Out of bounds error")
         return False

        if index == 0:
         return self.prepend(value)

        if index == self.length:
         return self.append(value)
        
        new_node = Node(value)
        temp = self.head
        #insert at index 3 means 0,1,2,"3" the node at index 3 gets pushed to index 4 since now this new node is the "3" index node
        for i in range(index-1):
           temp = temp.next
        new_node.next=temp
        temp.next = new_node
        self.length += 1
        return True
    

    def remove(self,index):
        if index < 0 or index >= self.length:
         print("Out of bounds error")
         return None

        if index == 0:
         return self.pop_first()

        if index == self.length-1:
         return self.pop()
        
        pre = self.head

        for i in range(index-1):
           pre = pre.next 

        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # def reverse(self):
       








my_linked_list = LinkedList(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
