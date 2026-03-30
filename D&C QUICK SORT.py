# D&C Quick sort
'''
10 7 8 9 1 5

pivot= reference point to biforcate some data in data into 2 parts

1. pivot = 5
2. 2 pointers i-> tracks smaller elements, j scans the array
1=-1
p=5
traverse:
    j      arr[i]   camparing   action
    0       10         >5         ignore
    1       7          >5        ignore
    2       8          >5         ignore
    3       9          >5       ignore
    4       1          <5       increase i and swap

3. 1 7 8 9 10 5

swap pivot with i+1

   1 5 8 9 10 7

left=[1]
right=[8 9 10 7]
4. pivot=7
  j    arr[i]    pivot    action
  0      8        >7        increase i, and swap
right=[7 9 10 8]  
   j    arr[i]    pivot    action
   0      7        >8        ignore
   1      9        <8        increase i, and swap
5. pivot=9
right=[7 8 10 9]  
   j    arr[i]    pivot    action
   0      7        >9        ignore
   1      8        >9        ignore
   3      10       <9       increase i, and swap
right=[7 8 9 10]

approach:
1. start with array.
2. chose pivot at the end of an array.
3. partition the elements,
   -move all elements smaller than pivot to left and greater tyhan pivot to right.
4. recursevely applyt D/C.
5. repeate until the values are sorted.
'''
#
'''
def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
def partition(arr,low,high):
    piviot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<piviot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
        
arr=list(map(int,input("enter elements into list:").split()))
quicksort(arr, 0, len(arr)-1)
print("sorted array:",arr)

out put:
    enter elements into list:10 7 8 9 1 5
    sorted array: [1, 5, 7, 8, 9, 10]
    
'''


def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
def partition(arr,low,high):
    piviot=arr[low]
    i=low
    for j in range(low+1,high+1):
        if arr[j]<piviot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[i]=arr[i],arr[low]
    return i
        
arr=list(map(int,input("enter elements into list:").split()))
quicksort(arr, 0, len(arr)-1)
print("sorted array:",arr)

