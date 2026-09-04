deque = []

n = int(input("Enter the number of elements: "))

while True:
    print("1. Add from Front")
    print("2. Add from Rear")
    print("3. Delete from Front")
    print("4. Delete from Rear")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(deque) == n:
            print("Deque Overflow")
        else:
            ele = int(input("Enter element: "))
            deque.insert(0, ele)

    elif choice == 2:
        if len(deque) == n:
            print("Deque Overflow")
        else:
            ele = int(input("Enter element: "))
            deque.append(ele)

    elif choice == 3:
        if len(deque) == 0:
            print("Deque Underflow")
        else:
            print("Deleted element:", deque.pop(0))

    elif choice == 4:
        if len(deque) == 0:
            print("Deque Underflow")
        else:
            print("Deleted element:", deque.pop())

    elif choice == 5:
        if len(deque) == 0:
            print("Deque is empty")
        else:
            for i in deque:
                print(i)

    elif choice == 6:
        break

    else:
        print("Invalid choice")