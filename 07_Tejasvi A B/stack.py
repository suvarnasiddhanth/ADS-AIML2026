stack=[]
n=int(input("Enter the numbe rof elements"))
while True:
    print("add an element    -- 1")
    print("Remove element    -- 2")
    print("Dispaly elements  -- 3")
    print("Exit              -- 4")

    choice=int(input("Enter your choice"))

    if choice==1:
        if len(stack)==n:

            print("STack overflow")
        else:
            ele=int(input("Enter the element to be added"))
            stack.append(ele)

    elif choice==2:
        if len(stack)==0:
            print("stack underflow")
        else:
            elem=stack.pop()
            print("Deleted element is :",elem)

    elif choice==3:
        if len(stack)==0:
            print("Stack is underflow") 
        else:
            for i in range(n-1):
                print(i,stack[i])
    elif choice==4:
        break
    else:
        print("Invalid choice")