import sys

n = int(input())
list = [0] *10001


for i in range(n) :
    m = int(sys.stdin.readline())
    list[m] += 1

for i in range(0, len(list)):
    if list[i] != 0 :
        for j in range(0,list[i]) :
            print(i)
