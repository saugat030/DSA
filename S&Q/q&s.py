class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
   def __init__(self,value):
    new_node = Node(value)
    self.first = new_node
    self.last = new_node
    self.length = 1

   def enqueue(self,value):
    new_node = Node(value)
    if self.length == 0 or self.first is None:
      print("Queue empty creating a new node.")
      self.first = new_node
      self.last = new_node
      self.length = 1
    else:
     self.last.next = new_node
     self.last = new_node
     self.length += 1

   def dequeue(self):
     if self.length == 0:
       print("No items in queue")
       return None
     else:
       temp = self.first
       self.first = self.first.next #This will also work if there are only 1 element in the queue since self.first wil be None after this and we make the last None ourself
       temp.next = None
       self.length -= 1
       if self.length == 0:  # If only one element in the queue:
        self.last = None
       return temp
       

queue = Queue(1)
