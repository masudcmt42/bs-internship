class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data
    def insert(self,data):
        if self.val:
            if self.val>data:
                if self.left==None: self.left=Node(data)
                else: self.left.insert(data)
            else:
                if self.right==None: self.right=Node(data)
                else: self.right.insert(data)
        else:
            self.val=data
    def search(self,data):
        if self.val==data: 
            print(data," is found in tree")
            return
        if self.val > data and self.left!=None: self.left.search(data)
        elif self.val<data and self.right!=None: self.right.search(data)
        else:
            print(data," is not found")
    def inorder(self):
        if self.left: self.left.inorder()
        print(self.val,sep=" ")
        if self.right is not None: self.right.inorder()
    def preorder(self):
        print(self.val)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()
    def postorder:
        if self.left: self.left.postorder()
        if self.right: self.right.postorder()
        print(self.val)






tree=Node(50)
tree.insert(90)
tree.insert(30)
tree.insert(35)
tree.insert(20)
tree.insert(34)
tree.insert(25)
tree.search(30)
tree.search(22)
tree.search(95)
tree.inorder()
print("preoder")
tree.preoder()
