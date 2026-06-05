class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
n1=Tree(1)
n2=Tree(2)
n3=Tree(3)
n4=Tree(4)
n5=Tree(5)
n6=Tree(6)
n7=Tree(7)
root=n1
n1.left=n2
n1.right=n3
n1.left.left=n4
n1.left.right=n5
n1.right.left=n6
n1.right.right=n7

#inorder
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

inorder(root)
print()
preorder(root)
print()
postorder(root)
print()