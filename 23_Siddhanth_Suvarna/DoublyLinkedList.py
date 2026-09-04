"""Checklist											Completed
	1. 			Display list								✓
		1.1 	Display list in reverse  					✓
	2. 			Insert					  					✗
		2.1 	Insert at the beginning 					✓
		2.1.1 	Insert bulk at the beginning 				✓
		2.2 	Insert at the end			 				✓
		2.2.1 	Insert bulk at the end						✓
		2.3 	Insert after given value					✗
		2.3.1 	Insert bulk after given value				✗
	3. 			Pop											✗
		3.1 	Pop from the beginning						✓
		3.2 	Pop from the end							✗
	4. 			Traverse from beginning						✗


"""
size = 0
debug = 0
class ListNode:
	def __init__(self, val: int):
		self.value = val
		self.next = None
		self.prev =None
def debugprint(nodepointer, loc: int):
	nodenext = nodepointer.next
	nodeprev = nodepointer.prev
	if loc == -1:
		try:
			print("Prev:", nodeprev.value, "<--", nodepointer.value)
		except AttributeError:
			print("AttributeError when checking prev value")
	else:
		try:
			print("Next:\t   ", nodepointer.value, "-->", nodenext.value)
		except AttributeError:
			print("AttributeError when checking next value")
def nomatchmsg(flag):
	if flag == 0:
		print("\nNo match found\n")
def sizeincrement():
	global size
	size += 1
def sizedecrement():
	global size
	size -= 1
def insertnodeatstart(val: int, head, tail):
	newNode = ListNode(val)
	newNode.next = head
	if head != None:
		if head.prev != None:
			newNode.prev = head.prev
		head.prev = newNode
		if debug: 
			debugprint(head, -1)
			debugprint(head, 1)
	if tail == None:
		tail = newNode
	head = newNode
	sizeincrement()
	return head, tail
def insertnodeatend(val: int, head, tail):
	newNode = ListNode(val)
	newNode.prev = tail
	if tail != None:
		if tail.next != None:
			newNode.next = tail.next
		tail.next = newNode
		if debug: 
			debugprint(head, -1)
			debugprint(head, 1)
	if head == None:
		head = newNode
	tail = newNode
	sizeincrement()
	return head, tail
def traverse(val, head):
	curr = head
	flag = 0
	while curr != None:
		if curr.value == val:
			flag = 1
			return curr
		curr = curr.next
	nomatchmsg(flag)
	return None
def insertafterfirstfoundnode(insertval, val, head, tail):
	curr = traverse(val, head)
	if curr != None:
		insertnodeatend(insertval, head, tail)
# Below doesn't work rn, fix later
#def insertafterlastfoundnode(insertval: int, val: int, head):
#	curr, prev = traverse(val, head)
#	while curr != None:
#		newcurr = curr
#		newprev = prev
#		curr, prev=traverse(val, curr.next)
#	temp=insertnodeatstart(insertval,head)
#	temp.next=newcurr.next
#	newcurr.next = temp
def popnode_head(head):
	nextnode = head
	nextnextnode = nextnode.next
	nextnextnode.prev = None
	head = nextnode.next
	sizedecrement()
	return head
def displaylist(head, tail):
	end = head
	print("\nSTART")
	while end != None:
		print(f" {end.value} {"<== Head" if end == head else ("<== Tail" if end == tail else "")}")
		print(" ^")
		print(" |")
		print(" v")
		end = end.next
	print("END\n")
def displaylist_reverse(head, tail):
	end = tail
	print("\nSTART")
	while end != None:
		print(f" {end.value} {"<== Head" if end == head else ("<== Tail" if end == tail else "")}")
		print(" ^")
		print(" |")
		print(" v")
		end = end.prev
	print("END\n")
def traverse_till_hit(val: int, head):
	end = head#displaylist_reverse(head, tail)
	flag=0
	while end != None:
		if end.value == val:
			print("",end.value,"<---")
			flag=1
		else:
			print("",end.value)
		print(" ^")
		print(" |")
		print(" v")
		end = end.next
	print("End")
	nomatchmsg(flag)
def deletefirstfoundnode(val: int, head):
		curr, prev = traverse(val, head)
		traverse_till_hit(val, head)
		flag=0
		if curr != None:
			prev.next = curr.next
			print(curr.value,"deleted.")
			flag=1
			return
		prev=curr			
		curr = curr.next
		print("End")
		nomatchmsg(flag)
def deletelastfoundnode(val: int, head):
		curr = head
		lastmatch=None
		prev=None
		traverse_till_hit(val, head)
		flag=0
		while curr != None:
			if curr.value == val:
				lastmatch=curr
				lastmatchprev=prev
				flag=1 if flag != 1 else flag
			prev=curr
			curr = curr.next
		nomatchmsg(flag)
		if flag == 1:#displaylist_reverse(head, taihead, tail = insertnodeatstart(63, head, tail)l)
			lastmatchprev.next = lastmatch.next
def deleteallnode(val: int, head):
		curr = head
		traverse_till_hit(val, head)
		flag=0
		while curr != None:
			if curr.value == val:
				previous = curr.prev
				previous.next = curr.next
				print(curr.value,"deleted.")
				flag=1			
			curr = curr.next
		print("End")
		nomatchmsg(flag)
def insertnode_multiple(l, end, head, tail):
	try:
		l=list(l)
		for x in l:
			head, tail = insertnodeatstart(x, head, tail) if end == 'Start' else insertnodeatend(x, head, tail)
	except TypeError:
		print(type(l),"is not iterable.")
	return head, tail
head = None
tail = None
l1 = [1,2,31,11]
head, tail = insertnode_multiple(l1, 'Start', head, tail)
head, tail = insertnode_multiple([77], 'End', head, tail)
head = popnode_head(head)
head, tail = insertnode_multiple([89, 63], 'Start', head, tail)
head,tail = insertnodeatend(55, head, tail)
#deleteallnode(7,head)
#deletelastfoundnode(7,head)
#traverse_till_hit(5,head)
insertafterfirstfoundnode(20,2,head, tail)
#insertafterlastfoundnode(2,7,head)
displaylist(head, tail)
#displaylist_reverse(head, tail)
print(size)