#calculate the number of nodes in a tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def countnodes(root):
    if not root:
        return 0
    return 1+countnodes(root.left)+countnodes(root.right)

root=node(int(input("enter root value:")))
root.left=node(int(input("enter left value:")))
root.right=node(int(input("enter right value:")))
root.left.left=node(int(input("enter left left value:")))
root.left.left.left=node(int(input("enter left left left value:")))
print("number of nodes in tree:",countnodes(root))