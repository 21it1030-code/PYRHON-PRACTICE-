#advanced hashing approaches
'''
hashing 2 pointer
sliding 2 pointer
'''

#write a code to find all unique quadraples such that a+b+c+d=target in given array
'''
arr=1 0 -1 0 -2 2
target=0
o/p:
    possible quadraplets
    [-2 -1 1 2]=0
    [-2 0 0 2]=0
    [-1 0 0 1]=0
    

arr =list(map(int,input("elements:").split()))
target=int(input("target : "))
arr.sort()
n=len(arr)
result=[]
for i in range(n-3):
    if i>0 and arr[i] ==arr[i-1]:
        continue
    for j in range(i+1,n-2):
        if j>i+1 and arr[j]==arr[j-1]:
            continue
        left=j+1
        right=n-1
        while left<right: 
            total=arr[i]+arr[j]+arr[left]+arr[right]
            if total==target:
                result.append([arr[i],arr[j],arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left]==arr[left-1]:
                    left-=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
            elif total<target:
                left+=1
            else:
                right-=1
for q in result:
    print(q)
'''

'''
eat,tea tan ate nat bat
[eat tea ate]
[tan nat]
[bat]

eat->sort
tea->sort
ate->sort
hashmap["ate"]-> [eat,tea,ate]
approach
1. words =[eat,tea tan ate nat bat]
2. create hash map
kay-> sorted word
val=list of words (anagramed)

example
hashmap["aet"]->[tea ate eat]
hashmap["ant"]->[nta tan]
hashmap["abt"]->[bat]
3.traverse every word
4.sort ->eat->aet
         tea->aet
5. append trhe word/ create a list and push themwrt their sorted order
6.print hash map values O(n* k log k)
'''

#write a code to segregate the anagrams wrt their lexiographical order and group them accordingly
'''
input=eat,tea tan ate nat bat
o/p:[eat tea ate]
[tan nat]
[bat]
'''
from collections import defaultdict
words =input("words:").split()
amp=defaultdict(list)
for word in words:
    key=' '.join(sorted(word))
    amp[key].append(word)
for group in amp.values():
    print(group)
