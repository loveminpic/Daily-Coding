import sys

input = sys.stdin.readline

num = int(input().strip())
count = 0
arr = set()
result = []
for i in range(num) :
    temp = input().strip()
    if temp == "ENTER" :
        count += len(arr)
        arr.clear()
    else :
        arr.add(temp)
        
count += len(arr)
print(count)