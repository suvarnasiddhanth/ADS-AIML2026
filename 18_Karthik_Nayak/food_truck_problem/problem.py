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
            copied=Node(current.data)

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

            current=current.next

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

    
def main():
    my_list=LinkedList()
    truck1=None
    truck2=None
    while True:
        print("Menu")
        print("1:insert person into queue")
        print("2.print original queue")
        print("3:divide queue into two trucks")
        print("4:print truck 1")
        print("5:print truct 2")
        print("6:serve queue(both trucks)")
        print("7:Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            data = input("Enter data to insert: ")
            my_list.insert(data)
            print(f"{data} inserted successfully.")

        elif choice == "2":
            print("Original Queue:")
            my_list.print_list()

        elif choice == "3":
            truck1, truck2 = my_list.divide_queue()
            print("Queue divided into Truck 1 and Truck 2.")

        elif choice == "4":
            print("Truck 1:")
            if truck1 is None:
                print("Truck 1 is empty. Divide the queue first (option 3).")
            else:
                LinkedList.print_from_head(truck1)

        elif choice == "5":
            print("Truck 2:")
            if truck2 is None:
                print("Truck 2 is empty. Divide the queue first (option 3).")
            else:
                LinkedList.print_from_head(truck2)

        elif choice == "6":
            if truck1 is None and truck2 is None:
                print("Trucks are empty. Divide the queue first (option 3).")
            else:
                print("Serving order:")
                my_list.serve_queue(truck1, truck2)

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()