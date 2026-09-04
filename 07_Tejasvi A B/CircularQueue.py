n = int(input("Enter the size of circular queue: "))

queue = [0] * n

front = -1
rear = -1

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if (rear + 1) % n == front:
            print("Circular Queue Overflow")

        else:
            ele = int(input("Enter element: "))

            if front == -1:
                front = 0
                rear = 0
            else:
                rear = (rear + 1) % n

            queue[rear] = ele

    elif choice == 2:

        if front == -1:
            print("Circular Queue Underflow")

        else:
            print("Deleted element:", queue[front])

            if front == rear:
                front = -1
                rear = -1
            else:
                front = (front + 1) % n

    elif choice == 3:

        if front == -1:
            print("Circular Queue is empty")

        else:
            print("Circular Queue elements:")

            i = front

            while True:
                print(queue[i])

                if i == rear:
                    break

                i = (i + 1) % n

    elif choice == 4:
        break

    else:
        print("Invalid choice")