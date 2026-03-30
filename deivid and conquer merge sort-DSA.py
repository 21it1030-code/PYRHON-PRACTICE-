# DIVIDE AND CONQUER
'''
DIVIDE AND CONQUER O(n logn)
1.merge sort
2.quick sort

practice:
tim sort -> insertion sort+ merge sort
heap sort


1. Merge sort

-> divide
-> conquer
-> Segregate and append

ALGORITHM:
1. take an array
2. find the mid of an anrray
3. divide the array into left and right halves
4. recursevely apply mergesort on both halves untill each element gets indepandent (only element)
5. when each subarray contains one element then break / stop dividing
6. compare each element with adjusent element on each half independently to get an independent sorted array on either side
7. repeat this merging process untill sorted array returns

'''
# write a code to perform merge sort

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]   #dividing left
        right=arr[mid:]  #dividing right
        mergesort(left)  
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right): # copying left and right values into array
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        # after sorting and coping the values left, right and arr are again intialize to i=j=k=0    
        while i<len(left):   # copying left values into array
            arr[k]=left[i]
            k+=1
            i+=1
        while j<len(right):  # copying left values into array
            arr[k]=right[j]
            k+=1
            j+=1

arr=list(map(int,input("enter elements into list:").split()))
mergesort(arr)
print(arr)

'''
out put:
enter elements into list:289 29783 1048 76089134 1 3249708 4 0862 45
[1, 4, 45, 289, 862, 1048, 29783, 3249708, 76089134]

'''
