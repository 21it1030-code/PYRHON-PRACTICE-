#write a code to find the length of longest consequtive sequence in an array and print the size of esquence
nums=list(map(int,input("values:").split()))
numset=set(nums)
long=0
for num in numset:
    if num-1 not in numset:
        curr=num
        length=1
        while curr+1 in numset:
            curr+=1
            length+=1
        long=max(long,length)
print(long)        
        
