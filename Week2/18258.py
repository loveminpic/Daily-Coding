import sys
import collections

num = int(sys.stdin.readline().strip())
queue = collections.deque()

for i in range(0, num) :
    command = list(map(str, sys.stdin.readline().split()))
    
    if command[0] == "push" :
        queue.append(command[1])
        
    elif command[0] == "pop" :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif command[0] == "size" :
        print(len(queue))
    
    elif command[0] == "empty" :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == "front" :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])
            
    elif command[0] == "back" :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[-1])  