import sys
import collections

input = sys.stdin.readline

n ,k = map(int, input().split())
queue= collections.deque()
arr = []
visted = [0] * (k+1)

for i in range(0, n):
    m = int(input().strip())
    queue.append(m)
    arr.append(m)

level = 0
check = True

while queue :
    if check == False :
        break 
    level += 1
    for j in range(0,len(queue)) :
        temp = queue.popleft()
        left = k - temp
        for i in range(0, len(arr)) :
            if left > arr[i] :
                if visted[temp+arr[i]] == 0 :
                    queue.append(temp+arr[i])
                    visted[temp+arr[i]] = 1
            elif left == arr[i] :
                level += 1
                check = False
                break
        if check == False :
            break
                      
if check == False :      
    print(level)
else :
    print(-1)