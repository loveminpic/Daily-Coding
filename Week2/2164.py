import collections
import sys

num = int(sys.stdin.readline().strip())
dequeue = collections.deque()

for i in range(1, num+1) :
    dequeue.append(i)

while len(dequeue) != 1 :
    dequeue.popleft()
    temp = dequeue.popleft()
    dequeue.append(temp)
    
    
print(dequeue.pop())