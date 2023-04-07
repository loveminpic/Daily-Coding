max = 0
count = 0
for i in range(0,9) :
    temp = int(input())
    if max < temp :
        max = temp
        count = i
        
print(max)
print(count+1)