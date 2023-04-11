import sys
from itertools import permutations

def check(list) :
    count =0 
    for i in range(0, len(list)-1) :
        count += abs(list[i] - list[i+1])
        
    return count
num = int(input())
data = list(map(int ,input().split()))
print(data)
list = list(permutations(data,num))

all_data = []

for i in range(0, len(list)) :
    all_data.append(check(list[i]))
    
print(max(all_data))
