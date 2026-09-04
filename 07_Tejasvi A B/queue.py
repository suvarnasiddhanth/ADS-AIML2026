queue=[]
n=int(input("Enter the number of elements"))
while True:
    print("add an element    -- 1")
    print("Remove element    -- 2")
    print("Display elements  -- 3")
    print("Exit              -- 4")

    choice=int(input("Enter your choice"))

    if choice==1:
        if len(queue)==n:
            print("Queue overflow")
        else:
            ele=int(input("Enter the element to be added"))
            queue.append(ele)

    elif choice==2:
        if len(queue)==0:
            print("Queue underflow")
        else:
            elem=queue.pop(0)
            print("Deleted element is :",elem)

    elif choice==3:
        if len(queue)==0:
            print("Queue is underflow") 
        else:
            for i in range(len(queue)):
                print(i,queue[i])
    elif choice==4:
        break
    else:
        print("Invalid choice")