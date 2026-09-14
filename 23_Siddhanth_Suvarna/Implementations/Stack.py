class Stack:
    def __init__(self,val=None, maxsize=None):
        self.value = []
        self.top = -1 if val == None else 0
        self.value.append(val)
        self.maxsize = maxsize
    def __repr__(self):
        return f"{self.value}"
    def push(self,val):
        if self.isFull() == True:
            return
        else:
            self.value.append(val)
            self.top += 1
    def pop(self):
        if self.isEmpty() == True:
            return
        else:
            self.value.pop()
            self.top -= 1
    def peek(self):
        if self.isEmpty() != True: 
            print(self.value[self.top])
    def size(self):
        return (self.top + 1)
    def isEmpty(self):
        if self.top == -1:
            print("Stack is empty.")
            return True
    def isFull(self):
        if self.top == (self.maxsize - 1):
            print("Stack is full.")
            return True
s = Stack("Hello", 5)
s.push("World,")
s.push(42)
s.push("is")
print(s)
s.pop()
s.peek()
print("Size of stack:",s.size())
s.push("is")
s.push("the secret.")
s.push("secret")
function_list = ["Push", "Pop", "Peek", "Size", "Display"]
from tkinter import *
from tkinter import ttk
root = Tk()
style = ttk.Style()
style.configure("Custom.TFrame", background="light blue")
frm = ttk.Frame(root, padding=10, border=10, style="Custom.TFrame")
frm.grid()
ttk.Label(frm, text="Stack", font="Calibri", background="light blue").grid(column=1,row=0, pady=15)
for index, function in enumerate(function_list, start=1):
    ttk.Button(frm, text=function, command=root.destroy, padding=10, width=20).grid(column=1, row=index)
ttk.Label(frm, text=s, font="Calibri", background="light blue").grid(column=1,row=index+3, pady=15)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=index + 2, pady=10)
root.mainloop()