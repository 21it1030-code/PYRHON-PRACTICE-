# HASH+ QUEUE
from collections import deque
stream =input("enter chars:")
freq={}
q= deque()
for ch in stream:
    freq[ch]=freq.get(ch,0)+1
    q.append(ch)
    print("\n queue before enque",list(q))
    while q and freq[q[0]]>1:
        removed=q.popleft()
        print("removed from queue:",removed)
    print("queue after removed :",list(q))
    if q:
        print("first non repeating char",q[0])
    else:
        print("first non repeating char -1")

#OUT PUT
'''
enter chars:aabc

 queue before enque ['a']
queue after removed : ['a']
first non repeating char a

 queue before enque ['a', 'a']
removed from queue: a
removed from queue: a
queue after removed : []
first non repeating char -1

 queue before enque ['b']
queue after removed : ['b']
first non repeating char b

 queue before enque ['b', 'c']
queue after removed : ['b', 'c']
first non repeating char b

'''

