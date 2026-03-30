'''deleting minimum element from min heap'''
import heapq
min_heap = []
n=int(input("enter number of nodes:"))
for i in range(n):
    val=int(input("enter value:"))
    heapq.heappush(min_heap,val)
print("before deletion min heap:",min_heap)
removed=heapq.heappop(min_heap)
print("after deletion of min heap:",min_heap)