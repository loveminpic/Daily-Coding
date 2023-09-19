import sys
from collections import deque

N = int(sys.stdin.readline().strip())
queue = deque()
for i in range(N):
    commend = sys.stdin.readline().split()
    if commend[0] == "push":
        queue.append(int(commend[1]))
    elif commend[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            temp = queue.popleft()
            print(temp)
    elif commend[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == "size":
        print(len(queue))
    elif commend[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif commend[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
