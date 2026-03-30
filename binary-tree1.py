# create a binary tree with user defined node whwre the root: 11 left:12 right:13
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root_val=int(input("enter root value:"))
root=node(root_val)
left_val=int(input("enter left value:"))
root.left=node(left_val)
right_val=int(input("enter left value:"))
root.right=node(right_val)
print("tree created successfully")
print("root:",root.data)
print("root left child:",root.left.data)
print("root right child:",root.right.data)