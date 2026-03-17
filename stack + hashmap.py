# stack + hashmap for performing the evaluation of stack operation using hash
'''
elements=6
1st=5
2nd=7
3rd=5
4th=7
6th=4
6th=5

before pop:
    freq=[5 7 4]
    freq=[5 7]
    freq=[5]
after pop:
    freq=[5 7 4]
    freq=[5 7]
    freq=[]   '''

from collections import defaultdict
freq=defaultdict(int)
stack =defaultdict(list)
max_freq=0
n=int(input("stack size:"))
for i in range(n):
    x=int(input("enter element:"))
    freq[x]+=1    #    freq[5]+=1    
    f=freq[x]      #   f=1
    stack[f].append(x)  #   stack[1]=[5]
    if f>max_freq:
        max_freq=f   #  max_freq=1   
print("\n before pop:")
for f in stack:
    print("frequency", f, ":", stack[f])

#pop operation
val=stack[max_freq].pop()
freq[val]-=1
print("\n element popped:",val)
print("after pop:")
for f in stack:
    print("frequency", f, ":", stack[f])

'''
# OUT PUT:
stack size:6
enter element:5
enter element:7
enter element:5
enter element:7
enter element:4
enter element:5

 before pop:
frequency 1 : [5, 7, 4]
frequency 2 : [5, 7]
frequency 3 : [5]

 element popped: 5
after pop:
frequency 1 : [5, 7, 4]
frequency 2 : [5, 7]
frequency 3 : []

'''

# DRY RUN
'''
freq={}
stack={}
max_freq=0

x=5
freq[5]=1
f=1
stack[1]=[5]
freq{5:1}
max_freq=1

x=7
freq[7]=1
f=1
stack[1]=[5,7]
freq{5:1, 7:1}
max_freq=1

x=5
freq[5]=1
f=1+1
stack[1]=[5,7,5]
freq{5:2, 7:1}
max_freq=2

x=5
freq[7]=1
f=1+1
stack[1]=[5,7,5,7]
freq{5:2, 7:2}
max_freq=2

x=4
freq[4]=1
f=1
stack[1]=[5,7,5,7,4]
freq{5:2, 7:2, 4:1}
max_freq=1

x=5
freq[5]=1
f=1+1+1
stack[1]=[5,7,5,7,4,5]
freq{5:3, 7:2, 4:1}
max_freq=3

freq{5:3, 7:2, 4:1}

'''























