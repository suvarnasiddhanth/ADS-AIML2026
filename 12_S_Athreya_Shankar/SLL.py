# Single Linked List

# Creation of a Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Merging the new nodes to the existing nodes in a linked list
class LinkedList:
    def __init__(self):
        self.head = None


    def display_linked_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end='=>')
            current_node = current_node.next
        print(None)


    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        # new_node.next = None # Optional, already initialised the next as None while creating


    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        count = 0
        current_node = self.head
        while count!=(position-1):
            current_node = current_node.next
            count += 1

        new_node.next = current_node.next
        current_node.next = new_node

        

    def delete_at_beginning(self):
        if self.head is None:
            # Empty LinekdList
            print('Linked List is Empty. Deletion Not Possible.')
            return

        self.head = self.head.next


    def delete_at_end(self):

        if self.head is None:
            # Empty LinekdList
                print('Linked List is Empty. Deletion Not Possible.')
                return
        elif self.head.next is None:
            # Single Node deletion from the LinekdList => Empty LinkedList after Node deletion
            self.head = None
            return

        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

        
    def delete_at_position(self, position):

        if self.head is None:
            # Empty LinekdList
                print('Linked List is Empty. Deletion Not Possible.')
                return 

        if position == 0:
            self.head = self.head.next
            return 
        
        count = 0
        current_node = self.head
        while count!=(position-1):
            current_node = current_node.next
            count += 1
        current_node.next = current_node.next.next
        return



    def search_key_value(self, key_value):
        found = False
        current_node = self.head
        position = 0
        if self.head is None:
            print('Linked List is Empty!')
            return
        while current_node is not None:
            if current_node.data == key_value:
                print('Key Value: ', key_value, " found in Linked List at position: ", position)
                found = True
            current_node = current_node.next
            position += 1

        if not found:
            print("Key Value: ", key_value, " is not found in the Linked List.")




linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
linked_list.insert_at_end(50)

linked_list.display_linked_list()

linked_list.insert_at_beginning(-10)
linked_list.insert_at_beginning(-20)
linked_list.insert_at_beginning(-30)
linked_list.insert_at_beginning(-40)
linked_list.insert_at_beginning(-50)

linked_list.display_linked_list()

linked_list.insert_at_position(900, 3)
linked_list.display_linked_list()


linked_list.delete_at_beginning()
linked_list.display_linked_list()

linked_list.delete_at_end()
linked_list.display_linked_list()

linked_list.delete_at_position(4)
linked_list.display_linked_list()


linked_list.search_key_value(80)
linked_list.display_linked_list()

linked_list.search_key_value(30)
linked_list.display_linked_list()