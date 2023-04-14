import sys

num = int(sys.stdin.readline().strip())
liq = list(map(int,sys.stdin.readline().split()))

liq.sort()

left = 0
right = num - 1

temp1 = 10000
temp2 = 10000

s = float("inf")

while left <= right :
    m = liq[left] + liq[right]
    if left == right :
        break
    if m < 0 :
        if abs(s) > abs(m):
            temp1 = liq[left]
            temp2 = liq[right]
            s = abs(m)
        left += 1
    elif m > 0 :
        if abs(s) > abs(m):
            temp1 = liq[left]
            temp2 = liq[right]
            s = m
        right -= 1
    elif m == 0 :
        temp1 =  liq[left]    
        temp2 =  liq[right]
        s = m
        break

print(temp1, temp2)