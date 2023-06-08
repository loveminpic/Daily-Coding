import sys
import collections
N = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

result = 0
count = 1

arr = sorted(arr)
for i in range(N) :
    for j in range(count) :
        result += arr[j]
    count+= 1
    
print(result)



# N = int(sys.stdin.readline().strip())
# arr = collections.deque(map(int,sys.stdin.readline().split()))

# result = 0
# count = 1
# list = []

# for i in range(N) :
#     temp = 0
#     for j in range(N) :
#         for h in arr[0:count] :
#             temp += h
        

# print(list)
