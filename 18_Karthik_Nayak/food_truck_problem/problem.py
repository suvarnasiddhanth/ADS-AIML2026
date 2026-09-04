class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def divide_queue(self):
        current = self.head
        turn = 1

        truck1_head = None
        truck1_tail = None
        truck2_head = None
        truck2_tail = None

        while current != None:
            # create copied node here
            copied=Node(current.data)

        # decide truck using turn
            if turn==1:
                if truck1_head==None:
                    truck1_head=copied
                    truck1_tail=copied
                else:
                    truck1_tail.next=copied
                    truck1_tail=copied
                turn=2
            else:
                if truck2_head==None:
                    truck2_head=copied
                    truck2_tail=copied
                else:
                    truck2_tail.next=copied
                    truck2_tail=copied
                turn=1

            # move current
            current=current.next

            # return the two truck lists
        return truck1_head, truck2_head

    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node

    def print_list(self):
        current=self.head
        while current!=None:
            print(current.data,end=" -> ")
            current=current.next
        print("None")


    def print_from_head(head):
        current = head
        while current != None:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

    def serve_queue(self, truck1, truck2):
        current_truck1 = truck1
        current_truck2 = truck2

        while current_truck1 != None or current_truck2 != None:
            if current_truck1 != None:
                print(f"Serving person {current_truck1.data}")
                current_truck1 = current_truck1.next
            
            if current_truck2 != None:
                print(f"Serving person {current_truck2.data}")
                current_truck2 = current_truck2.next

    

my_list = LinkedList()

my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.insert(40)
my_list.insert(50)
my_list.insert(60)

truck1, truck2 = my_list.divide_queue()

print("Original Queue:")
my_list.print_list()

print("Truck 1:")
LinkedList.print_from_head(truck1)

print("Truck 2:")
LinkedList.print_from_head(truck2)

print("Serving order:")
my_list.serve_queue(truck1, truck2)