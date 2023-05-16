import sys

input = sys.stdin.readline
all, a, b = map(int, input().split())

if a > b :
    temp = a 
    a = b
    b = temp

count = 1

while all > 1 :
    if abs(a - b) == 1 and a % 2 ==1 and b % 2 == 0 :
        break 
    else :
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        all = all / 2
        count += 1

print(count)
        