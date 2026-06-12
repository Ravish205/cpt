class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n1,n2,n3=Tree(1),Tree(2),Tree(3)
n1.left,n1.right=n2,n3
root=n1
count=sum=0
max=min=root.val
def countnode(root):
    global count
    if root is None:
        return
    count+=1
    countnode(root.left)
    countnode(root.right)
def sumnode(root):
    global sum
    if root is None:
        return
    sum+=root.val
    sumnode(root.left)
    sumnode(root.right)
def maxnode(root):
    global max
    if root is None:
        return
    if root.val > max:
        max=root.val
    maxnode(root.left)
    maxnode(root.right)
def minnode(root):
    global min
    if root is None:
        return
    if root.val < min:
        min=root.val
    minnode(root.left)
    minnode(root.right)
def print_depth(root,depth):
    if root is None:
        return
    print("elements: ",root.val,"depth: ",depth)
    print_depth(root.left,depth+1)
    print_depth(root.right,depth+1)
countnode(root)
print(count)
sumnode(root)
print(sum)
maxnode(root)
print(max)
minnode(root)
print(min)
print_depth(root,0)