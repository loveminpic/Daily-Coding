import sys
import math

input = sys.stdin.readline
num = int(input().strip())

dic = {}
list = []

for i in range(num) :
    temp = int(input().strip())
    if temp in dic :
        dic[temp] += 1
    else :
        dic[temp] = 0
    list.append(temp)

print(round(sum(list)/len(list)))

list = sorted(list)

mi = list[0]
mx = list[-1]

midi = len(list)//2

m = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(list[midi])

if len(list) == 1 :
    print(m[0][0])
else :
    if m[0][1] == m[1][1] :
        print(m[1][0])
    else :
        print(m[0][0])

        
print(mx-mi)
