class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.count=0

    def push(self,x):
        newNode=Node(x)
        newNode.next=self.top
        self.top=newNode
        self.count+=1

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        self.temp=self.top
        self.top=self.top.next
        val=self.temp.data
        self.count-=1

        del self.temp
        return val

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.count

if __name__ == "__main__":
    st = Stack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    # popping one element
    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")

    # checking current size
    print("Current size:", st.size())
    
        
