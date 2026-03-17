#write a code to search an element using two pointer one way and print the element
'''
print(1)
arr=list(map(int,input("elements:").split()))
slow=0
fast=0
while fast<len(arr) and fast+1<len(arr):
    slow+=1
    fast+=2
print("middle element:",arr[slow])    '''



#write a code to detect a duplicate using index array jumping (floyd's algo concept)
'''
print(2)
arr=list(map(int,input("elements:").split()))
slow=arr[0]
fast=arr[0]
while True:
    slow=arr[slow]
    fast=arr[arr[fast]]
    if slow==fast:
        break
slow=arr[0]
while slow!=fast:
    slow=arr[slow]
    fast=arr[fast]
print("duplicate :",slow)   '''

#write a code to find the sum of longest subarray /////////<=k using sliding window with 2 pointer approach
#arr=[1,2,1,0,1,1,0]
#4
print(3)
arr=list(map(int,input("elements:").split()))
k=int(input("enter slide size k:"))
slow=0
sum=0
maxlen=0
for fast in range(len(arr)):
    sum+=arr[fast]
    while sum>k:
        sum-=arr[slow]
        slow+=1
    maxlen=max(maxlen,fast-slow+1)
print("maxlen:",maxlen)    
