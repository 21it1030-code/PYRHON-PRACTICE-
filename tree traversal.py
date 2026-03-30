class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")                

root = node(int(input("enter root value:")))
root.left = node(int(input("enter left value:")))
root.right = node(int(input("enter right value:")))
print("inorder treaversal",postorder(root))        # change tree traversal method here inorder, preorder, postorder
