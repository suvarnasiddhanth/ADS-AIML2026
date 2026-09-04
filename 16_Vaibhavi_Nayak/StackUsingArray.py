class Stack:
    def __init__(self,cap):
        self.arr=[0]*cap
        self.capacity=cap
        self.top=-1

    def push(self,data):
        if self.top==self.capacity-1:
            print("Stack is full")
            return -1
        else:
            self.top+=1
            self.arr[self.top]=data

    def pop(self):
        if self.top==-1:
            print("Stack is empty")
            return -1
        else:
            value=self.arr[self.top]
            self.top-=1
            return value
            

    def isEmpty(self):
        return self.top==-1

    def isFull(self):
        return self.top==self.capacity-1

    def peek(self):
        if self.top==-1:
            print("Stack is empty")
            return -1
        val=self.arr[self.top]
        return val

if __name__=="__main__":
    st=Stack(4)
    st.push(10)
    st.push(20)
    st.push(50)
    st.push(60)
    st.push(70)
    print(st.isFull())
    print("Stack top : ",st.peek())
    st.pop()
    print("Stack top : ",st.peek())
    print(st.isEmpty())
    print(st.isFull())
    st.pop()
    st.pop()
    print(st.isEmpty())

        

        

