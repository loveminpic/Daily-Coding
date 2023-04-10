# 합이 100..
import sys
data = [int(sys.stdin.readline().strip()) for i in range(0,9)]

m = sum(data) - 100
check = True

for i in range(0,9):
    for j in range(i+1,9) :
        if data[i] + data[j] == m :
            temp1 = data[i]
            temp2 = data[j]
            data.remove(temp1)
            data.remove(temp2)
            check = False
            break
    if(check == False) :
        break
data.sort()

for i in range(len(data)):
    print(data[i])