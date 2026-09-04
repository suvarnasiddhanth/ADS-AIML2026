# Create a node
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class single_linked_list:
    def __init__(self):
        self.head = None           # intially the node is empty

# insert at the beginning
    def insert_begin(self,data):
        new_node = Node(data)      # create a new node
        new_node.next = self(head) # new node points to the current first node
        self.head = new_node       # make the new node the first node         

# insert at the ending
    def insert_end(self,data):
        new_node = Node(data)        
        if self.head is empty:     #if list is empty new node becomes head
            new_node = self(head)
            return
        temp = self.next           # start from first node
        while temp.next is not None:
            temp = temp.next       # move until we reach the last node
        temp.next = new_node       # last node points to the new node

# insert after a specific node
    def insert_after(self,key,data):
        temp = self.head           # start from the first node
        while temp is not None and temp.data ! = key:  # search for the node containing key
            temp = temp.next
                                   # if node is not found
        if temp is None:
            print("node not found")
            return    
        new_node = Node(data)     # create a new node
        new_node_next = temp.next # new node points to the next node
        temp.next = new_node

# delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next # move head to the next node

# delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty") 
            return
        if self.head.next is None: # if there is only one node
            self.head = None
            return        
        temp = self.head         # start from the first node
        while temp.next.next is not None: # move to the second last node
            temp = temp.next
            temp.next = None  # remove the connection to the last node

 # delete from specific node
    def delete(self,key):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == key:   # if the first node contains the key
            self.head = self.head.next  
        temp = self.head
        while temp.next is not None and temp.next.data ! = key:
            tempt = temp.next   
        if temp.next is None:  # if the target node is not found
            print("list is empty")
            return
        temp.next = temp.next.next #skip the node that needs to be deleted

# search for an element
    def element(self,key):
        temp = self.head
        while temp is not None:  # traverse the list
            if temp.data == key:
                return True     # check if current node contains the key
            temp = temp.next
        return false          

# display the list
    def display(self):
        if self.head is None:
            print(""list is empty)
            return    
        
                



        