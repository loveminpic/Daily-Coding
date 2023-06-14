import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())
arr = []
less = 10000000000

sour = 0
bitter = 0
        
for i in range(N) :
    arr.append(list(map(int,input().split())))

com = []
for i in range(1, N+1):
    com.append(list(combinations(arr, i)))
    
print(com)