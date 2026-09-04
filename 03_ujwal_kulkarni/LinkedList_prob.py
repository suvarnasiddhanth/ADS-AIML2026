class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_people(self, person):
        if self.head is None:
            self.head=Node(person,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(person,None)
    def display(self,head):
        itr =head
        while itr:
            print(itr.data, end="-->")
            itr=itr.next
        print("NULL")

    def split(self):
        if self.head is None:
            print("empty List")
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        second_half = slow.next
        slow.next=None
        print("Counter 1:")
        self.display(self.head)
        print("Counter 2:")
        self.display(second_half)


people = LinkedList()

n = int(input("Enter number of people: "))

for i in range(1, n + 1):
    people.insert_people(i)

print("\nOriginal Queue:")
people.display(people.head)

people.split()