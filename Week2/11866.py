import collections
import sys

N, K = map(int, sys.stdin.readline().split())
deque = collections.deque()

for i in range(1, N+1) :
    deque.append(i)

stack = collections.deque()
count = 0
while len(deque) != 0 :
    deque.rotate(-K +1)
    stack.append(deque.popleft())
    
print("<",end="")
for j in range(N-1):
    print(stack[j], end=", ")   
print("{0}>".format(stack[-1]))