import heapq
'''
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,30)
heapq.heappush(heap,40)    
print(heap)
x= heapq.heappop(heap)
print("removed:",x)
print("remaining heap:",heap)
y = heapq.heappop(heap)
print("removed:",y)
print("remaining heap:",heap)
heapq.heappush(heap,10)
print(heap)
'''
import heapq
heap=[5,10,20]
heapq.heapify(heap)
print(heap)
print(heapq.heappushpop(heap,7))
print(heap)
