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
import inspect
size = 0
debug = 0
head = None
tail = None
class ListNode:
	def __init__(self, val: int, nextnode=None, prevnode=None):
		self.value = val
		if nextnode != None:
			nextnode.prev = self
			self.next = nextnode
		else:
			self.next = None
		if prevnode != None:
			prevnode.next = self
			self.prev = prevnode
		else:
			self.prev =None
def DebugPrint(nodepointer, loc=0):
	nodenext = nodepointer.next
	nodeprev = nodepointer.prev
	if loc == -1:
		try:
			print(f"Prev: {nodeprev.value:5} <-- {nodepointer.value}")
		except AttributeError:
			print("AttributeError when checking prev value.")
	elif loc == 1:
		try:
			print(f"Next:\t\t{nodepointer.value} --> {nodenext.value}")
		except AttributeError:
			print("AttributeError when checking next value.")
	else:
		try:
			print("Curr:\t   ", nodepointer.value)
		except AttributeError:
			print("AttributeError when checking current node value.")
def NoMatchMsg(flag):
	if flag == 0:
		print("\nNo match found\n")
def sizeincrement():
	global size
	size += 1
def sizedecrement():
	global size
	size -= 1
def assignhead(node):
	global head
	head = node
def assigntail(node):
	global tail
	tail = node
#Function to add node in front of specified node
def InsertNodeInFront(val: int, before=None):
	global head, tail
	#If no node is passed, take head as default value
	before = head if before is None else before
	#If first arg is not None or the head, take note of the prev node
	if before!=None and before.prev !=None: previous=before.prev
	else: previous = None    #Required?
	newNode = ListNode(val, before, previous)
	if head == None or newNode.next == head: assignhead(newNode)
	if tail == None: assigntail(newNode)
	if debug: 
		DebugPrint(before, -1)
		DebugPrint(before, 1)
	sizeincrement()
	return newNode
def InsertNodeBehind(val: int, after=None):
	global head, tail
	after = tail if after is None else after
	if after!=None and after.next !=None: nextnode=after.next
	else: nextnode = None
	newNode = ListNode(val, nextnode, after)
	if head == None: assignhead(newNode)
	if tail == None or newNode.prev == tail: assigntail(newNode)
	if debug: 
		DebugPrint(tail, -1)
		DebugPrint(tail, 1)
	sizeincrement()
	return newNode
def traverse(val, head):
	curr = head
	flag = 0
	while curr != None:
		if curr.value == val:
			flag = 1
			return curr
		curr = curr.next
	NoMatchMsg(flag)
	return None
def insertafterfirstfoundnode(insertval, val):			#Wrong
	curr = traverse(val, head)
	if debug == 1: DebugPrint(curr)
	if curr != None:
		x,y = InsertNodeBehind(insertval, head, curr)
		temp = y.next
		temp.prev = y
def insertafterlastfoundnode(insertval: int, val: int, head): #Wrong
	curr, prev = traverse(val, head)
	while curr != None:
		newcurr = curr
		newprev = prev
		curr, prev=traverse(val, curr.next)
	temp=InsertNodeInFront(insertval,head)
	temp.next=newcurr.next
	newcurr.next = temp
def popnode_head():
	global head
	if head == None:
		print("Emply list, nothing to pop.")
		return
	nextnode = head.next
	if nextnode != None:
		nextnode.prev = None
	assignhead(nextnode)
	if nextnode == None:
		assigntail(nextnode)
	sizedecrement()
def displaylist():
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
	NoMatchMsg(flag)
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
		NoMatchMsg(flag)
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
		NoMatchMsg(flag)
		if flag == 1:#displaylist_reverse(head, taihead, tail = InsertNodeInFront(63, head, tail)l)
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
		NoMatchMsg(flag)
def InsertMultipleNode(l, pos, InsertInGivenOrder = None, start =None):
	global head, tail
	start = head if start is None else start
	try:
		l=list(l)
		newstart = InsertNodeInFront(l[0],start) if pos == 'Start' else InsertNodeBehind(l[0])
		if InsertInGivenOrder != None:
			for x in l[1:]:
				newstart = InsertNodeBehind(x, newstart)
		else:
			for x in l[1:]:
				newstart = InsertNodeInFront(x,newstart)
	except TypeError:
		print(type(l),"is not iterable.")
	return newstart
l1 = [1,2,31,61]
neww=InsertNodeInFront(100)
InsertNodeInFront(150)
InsertNodeInFront(200, neww)
InsertNodeBehind(266)
InsertNodeBehind(50,neww)
InsertMultipleNode(l1, 'Start')
InsertMultipleNode([77], 'End')
#popnode_head()
InsertMultipleNode([89, 63, 999, 888], 'Start', -1, neww)
#InsertNodeBehind(2)
#deleteallnode(7,head)
#deletelastfoundnode(2,head)
#traverse_till_hit(5,head)
#insertafterfirstfoundnode(20,2)
#insertafterlastfoundnode(2,7,head)


displaylist()
#displaylist_reverse(head, tail)
#print(size)
