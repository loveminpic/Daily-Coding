import sys

num = int(sys.stdin.readline().strip())
stick = [int(sys.stdin.readline().strip()) for i in range(num)]
count = 1

first = stick[-1]
temp = 0

for i in reversed(range(len(stick))) :
    if stick[i] > first and temp < stick[i]:
        count+= 1
        temp = stick[i]

print(count)