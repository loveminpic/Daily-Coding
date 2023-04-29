import sys
from collections import deque

cal = sys.stdin.readline().strip()
queue = deque()

queue = cal.split('-')


for i in range(0,len(queue)) :
    result = 0 
    temp = queue[i].split("+")
    if len(temp) > 1 :
        for j in range(0, len(temp)) :
            result += int(temp[j])
        queue[i] = result
        

result = 0
for i in range(1,len(queue)):
    result = result + int(queue[i])
        
print(int(queue[0])-result)    
