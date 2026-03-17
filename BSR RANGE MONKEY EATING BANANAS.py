# MONKEY EATING BANANAS
#write a code to find the min speed of eating, so the monkey eats all bananas in hour using BSR approach
#banana piles=3 6 7 11
#hour=8
#3->1hr
#6->2hr
#7->3hr
#11->4hr

piles=list(map(int, input("enter piles:").split()))
h=int(input("hours:"))
low=1
high=max(piles)
print(high)
ans=high
while low<=high:
    mid=(low+high)//2
    hours=0
    for p in piles:
        if p%mid==0:
            hours+=p//mid
        else:
            hours+=(p//mid)+1
    if hours<=h:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("minimum eating speed:",ans)        
