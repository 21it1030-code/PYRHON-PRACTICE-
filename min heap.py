# MIN HEAP

import heapq
'''
min_heap = []
n=int(input("enter number of nodes:"))
for i in range(n):
    val=int(input("enter value:"))
    heapq.heappush(min_heap,val)
print("min heap:",min_heap)
print("minimum element:",min_heap[0])
'''
def Tree(heap):
    n=len(heap)
    level=0
    i=0
    while i <n:
        nodes=2**level
        spaces=" "*(2**(4-level))
        print(spaces,end="")    
        count=0
        while count < nodes and i < n:
            print(heap[i],end=spaces)
            i+=1
            count+=1
        print("\n")
        level+=1
min_heap = []
n=int(input("enter number of nodes:"))
for i in range(n):
    val=int(input("enter value:"))
    heapq.heappush(min_heap,val)
print("min heap:",min_heap)
Tree(min_heap)
print("minimum element:",min_heap[0])