# array + hashmap find the first repeating element in array data structure
arr=list(map(int,input("elements:").split()))
freq={}
for num in arr:
    if num in freq:
        print("first repeating element:",num)
        break
    freq[num]=1
else:
    print("no repeating elements:")
