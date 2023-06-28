import sys
import collections

input = sys.stdin.readline
N = int(input().strip())
arr = {}
temp = []
for i in range(N) :
    temp = input().split()
    arr[int(temp[0])] = (int(temp[1]), int(temp[2]))
    
arr = sorted(arr.items(), key = lambda x : x[1][0], reverse=True)

for i in range(N) :
    