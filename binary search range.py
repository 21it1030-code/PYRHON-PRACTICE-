#wirte a code to performe binary search in range and print the range of search.
'''
arr=list(map(int,input("enter anumber:").split()))
arr.sort()
print(arr)
target=int(input("target:"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    print("Range:",low, "to",high)
    if arr[mid]==target:
        print("element found at index:",mid)
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
else:
        print("element not found!!!")
'''

'''
#find the square root valuue by bsr search
n=int(input("enter n:"))
low=0
high=n
ans=0
while low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print("square root:",ans   )        
      '''

# write a code to calaulate the minimum capacity of a ship where you have packages with weights you have to shipthem within d days
# input=[,1,2,3,4,5,6,7,8,9,10]
# d=5
# o/p:15
# min.capacity=max(w)=10
# max.capacity=sum(w)=55
# l=min.capacity
# h=max.capacity
'''
we=list(map(int,input("enter wights:").split()))
days=int(input("enter days:"))
low=max(we)
h=sum(we)
ans=h
while low<=h:
    mid = (low+h)//2
    d=1
    curr=0
    for w in we:
        if curr+w>mid:
            d+=1
            curr=0
        curr+=w    
    if d<=days:
        ans=mid
        h=mid-1
    else:
        low=mid+1
print("min capacity:",ans)     
        
