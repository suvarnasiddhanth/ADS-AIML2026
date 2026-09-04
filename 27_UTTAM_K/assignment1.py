class CustomerNode:
    def __init__(self, number):
        self.number = number
        self.next = None

class FoodTruckLine:
    def __init__(self, truck_name):
        self.truck_name = truck_name
        self.head = None
        self.tail = None

    def join_line(self, number):
        new_customer = CustomerNode(number)
        if self.tail is None:
            self.head = self.tail = new_customer
            return

        self.tail.next = new_customer
        self.tail = new_customer

    def serve_customer(self):
        if self.head is None:
            return f"{self.truck_name}: No one is in line."

        served_number = self.head.number
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return f"{self.truck_name} served customer #{served_number}"

    def get_line_string(self):
        numbers = []
        current = self.head
        while current:
            numbers.append(str(current.number))
            current = current.next
        return " -> ".join(numbers) or "Empty"

    def display_line(self):
        print(f"{self.truck_name} Line: {self.get_line_string()}")


def dispatch_customers(main_line_list):
    trucks = (FoodTruckLine("Truck A"), FoodTruckLine("Truck B"))

    current = main_line_list.head
    customer_index = 0

    while current:
        trucks[customer_index % 2].join_line(current.number)
        current = current.next
        customer_index += 1

    return trucks[0], trucks[1]



huge_main_line = FoodTruckLine("Main Event Line")

for i in range(1, 8):  # Customers 1 through 7
    huge_main_line.join_line(i)

print("BEFORE DISPATCH:")
huge_main_line.display_line()


print("\n--- Dispatching Crowd ---\n")
truck_a, truck_b = dispatch_customers(huge_main_line)

print("AFTER DISPATCH:")
truck_a.display_line()


truck_b.display_line()


print("\n--- Serving Food ---\n")
print(truck_a.serve_customer())


print(truck_b.serve_customer())

print("\nREMAINING LINES:")
truck_a.display_line()
truck_b.display_line()