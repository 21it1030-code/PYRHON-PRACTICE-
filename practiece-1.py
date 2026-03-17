#1palindrome
#2parfect num
#3
#LINKED LIST
'''
print(1,"linked list")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_begin(self,value):
        new_node = node(value)   # Create new node
        new_node.next = head  # Point new node to current head
        return new_node
        
def insert_end(head,value):
    new_node=node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:#always at end
        temp=temp.next
    temp.next=new_node
    return head

def delete_end(head):
    if head is None:#if empty
        print("empty")
        return None
    if head.next is None:
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head

def print_list(head):
    temp=head
    while temp:
        print(temp.data,end='->')
        temp=temp.next
    print("Tail")
    
def search(head,key):
    pos=1
    temp=head
    while temp:
        if temp.data==key:
            return pos
        temp=temp.next
        pos+=1
    return -1
head=None
n=int(input("enter nodes:"))
for i in range(n):
    val = int(input("enter value for begin:"))
    head= insert_begin(head,val)

n=int(input("enter nodes:"))
for i in range(n):
    val = int(input("enter value for end:"))
    head= insert_end(head,val)
    
key=int(input('enter element tio search:'))
p=search(head,key)

if p!=-1:
    print("element fount at position:",p)
else:
    print("not found")
print("single linked list before delete:",print_list(head))
head=delete_end(head)
print("single linked list after delete:",print_list(head))
'''
#write a code to print the first and last letter of word capital'
'''
a = ["prakash", "apple", "sdkjfghdsi", "ksjdfheiw"]
for word in a:
    res=word[0].upper() + word[1:-1] +word[-1].upper()
    print(res,end=' ')
'''
#
b = ["prakashlam", "apple", "sdkjfghdsi", "ksjdfheiwkjbuj"]    
b.sort()
print(b)#alphabetic order
b.sort(key=len)
print(b)#length
