# write a code to calaulate the minimum capacity of a ship where you have packages with weights you have to shipthem within d days
# input=[,1,2,3,4,5,6,7,8,9,10]
# d=5
# o/p:15
# min.capacity=max(w)=10
# max.capacity=sum(w)=55
# l=min.capacity
# h=max.capacity

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
        
