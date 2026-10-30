class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:
    
    def __init__(self):
        self.root = None

    def insert_node(self, data):
    
        newNode = TreeNode(data)
    
        if not self.root:
            self.root = newNode
            return self.root
        
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = newNode
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = newNode
                    break
                current = current.right
        
        return self.root
    
    def display(self):
        
        if not self.root:
            print("Tree is empty.")
            return
        
        queue = [self.root]
        head = 0
        result= []
        
        while head < len(queue):
            current = queue[head]
            head += 1
            
            result.append(current.data)
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        print("Level Order Traversal : ", result)
        
    def preorder(self, node, result):
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        
    def inorder(self, node, result):
            if node:
                self.inorder(node.left, result)
                result.append(node.data)
                self.inorder(node.right, result)
    
    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)
            
    def display_preorder(self):
            result = []
            self.preorder(self.root, result)
            print("Preorder Traversal : ", result)
            
    def display_inorder(self):
            result = []
            self.inorder(self.root, result)
            print("Inorder Traversal : ", result)
    
    def display_postorder(self):
            result = []
            self.postorder(self.root, result)
            print("Postorder Traversal : ", result)
            
    def get_height(self, node):
        if not node:
            return 0
        
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        
        return 1 +(left if left > right else right)
if __name__ == '__main__':

    bt = Binary_Search_Tree()

while(True):
    
    print("\nBinary Search Tree (BST) Operations : ")
    print("\n1. Insert Node\n2. Level Order Traversal\n3. Preorder Traversal\n4. Inorder Traversal\n5. Postorder Traversal\n6. Get Tree Height\n7. Quit")
    
    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid Choice\n")
        continue          
    
    match choice:

        case 1 : 
            element = int(input("Enter an element to insert in BST : "))
            bt.insert_node(element)
        case 2:
            bt.display()
        case 3:
            bt.display_preorder()
        case 4 : 
            bt.display_inorder()
        case 5 : 
            bt.display_postorder()
        case 6 :
            height = bt.get_height(bt.root)
            print("Height of the binary tree : ", height)
        case 7 : 
            break
        case _ : 
            print("Invalid Choice")
            
print("Program exited Successfully.")    


