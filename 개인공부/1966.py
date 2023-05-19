import sys
import collections
input = sys.stdin.readline

case = int(input().strip())

for i in range(case) :
    n, m = map(int, input().split())
    temp= list(map(int,input().split()))
    count = 1
    queue = collections.deque()
    
    for h in temp :
        queue.append((count,h))
        count += 1
    
    check = queue[m]
    count = 0
    temp_2 = ()
    
    while temp_2 != check :
        for j in range(len(queue)) :
            mx = max(queue, key=lambda item: item[1])
            temp_2 = queue.popleft()
            if temp_2 == mx:
                count +=1
                break
            else :
                queue.append(temp_2)
        if check == temp_2 :
            break
    print(count)