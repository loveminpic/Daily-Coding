import sys
import math

N = int(sys.stdin.readline().strip())
result = N

def check(n) :
    for i in range(2,int(n**(1/2))+1) :
        if n % i == 0 :
            return False
    return True
count = 2
while check(result) != True :
    if result % count == 0 and check(count) == True :
        result = result / count
        print(count)
        count = 2
    else :
        count += 1

print(int(result))