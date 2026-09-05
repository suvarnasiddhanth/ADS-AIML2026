# Doubly Linked List

# Creation of a Node
class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# Merging the new nodes to the existing nodes in a linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def display_linked_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end='<=>')
            current_node = current_node.next
        print(None)


    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        
        
    def insert_at_position(self, data, position):
    
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
                
        count = 0
        current_node = self.head

        while count!=(position-1):
            current_node = current_node.next
            count += 1

        new_node.next = current_node.next
        new_node.prev = current_node

        if current_node.next is not None:
            current_node.next.prev = new_node
        else:
            self.tail = new_node

        current_node.next = new_node

        

    def delete_at_beginning(self):
        if self.head is None:
            # Empty LinekdList
            print('Linked List is Empty. Deletion Not Possible.')
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None


    def delete_at_end(self):

        if self.head is None:
            print('Linked List is Empty. Deletion Not Possible.')
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

        
    def delete_at_position(self, position):

        if self.head is None:
            print('Linked List is Empty. Deletion Not Possible.')
            return

        if position == 0:
            self.delete_at_beginning()
            return

        count = 0
        current_node = self.head

        while count != position:
            current_node = current_node.next
            count += 1

        if current_node == self.tail:
            self.delete_at_end()
            return

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev



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