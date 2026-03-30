#search for a value in a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,key):
    if not root:
        return False
    if root.data==key:
        return True
    return search(root.left,key) or search(root.right,key)

root=node(int(input("enter root value:")))
root.left=node(int(input("enter left value:")))
root.right=node(int(input("enter right value:")))
root.left.left=node(int(input("enter left left value:")))
root.left.left.left=node(int(input("enter left left left value:")))
key=int(input("enter value to search in tree:"))
if search(root,key):
    print("value found in tree")
else:
    print("value not found in tree")
