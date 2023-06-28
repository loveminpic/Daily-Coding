import sys
import math
input = sys.stdin.readline

A,B = map(int,input().split())
sqrt_B = int(math.sqrt(B)+1)

check_prime = [True for _ in range(sqrt_B)] 
check_prime[0] = check_prime[1] = False

for i in range(2, sqrt_B) :
    if check_prime[i] == True :
        for j in range(i*2, sqrt_B, i) :
            check_prime[j] = False
        
count = 0
for i in range(2, sqrt_B) :
    if(check_prime[i] == True) :
        n = 2
        result = i ** n
        while(result <= B) :
            if result >= A :
                count += 1
            n += 1
            result = i ** n

print(count)