
import sys
from itertools import permutations

num = int(input())
data = []
how_many_city = []

for i in range(0, num):
    how_many_city.append(i)

for i in range(0, num) :
    data.append(list(map(int,sys.stdin.readline().split())))

check_list = list(permutations(how_many_city,num))
all_data = []
min = 1000000000

for i in range(0,len(check_list)):
    check = True
    count = 0
    for j in range(0,num):
        m = data[check_list[i][j]][check_list[i][(j+1)%num]]
        if m == 0 :
            count += 1999999
        count += m
        if count >= min :
            check = False
            break
    if check == True :
        if count < min :
            min = count

print(min)


