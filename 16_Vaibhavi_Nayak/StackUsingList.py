class Stack:
    def __init__(self):
        self.st=[]

    def push(self,x):
        self.st.append(x)

    def pop(self):
        if not self.st:
            print("Empty Stack")
            return -1
        return self.st.pop()

    def isEmpty(self):
        return len(self.st)==0

    def peek(self):
        if not self.st:
            print("Stack is empty")
            return -1
        return self.st[-1]

    def size(self):
        return len(self.st)


if __name__=="__main__":
    st=Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.push(50)
    print("Popped:", st.pop())
    print("Top element:", st.peek())
    print("Current size:", st.size())
    print("Stack is Empty ?",st.isEmpty())

    


    
