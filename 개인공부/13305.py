import sys

input = sys.stdin.readline

city = int(input().strip())
km = list(map(int,input().split()))
gas = list(map(int,input().split()))
minimum = gas[0]
result = 0

for i in range(0,city-1):
    minimum = min(minimum,gas[i])
    result += minimum * km[i]
     
    
print(result)