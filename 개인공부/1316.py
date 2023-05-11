import sys 

input = sys.stdin.readline
num = int(input().strip())

arr = []
count = 0
for i in range(num) :
    arr.append(input().strip())
    
for j in range(num):
    temp_arr = []
    for h in range(len(arr[j])):
        
        if arr[j][h] not in temp_arr :
            temp_arr.append(arr[j][h])
        elif arr[j][h] in temp_arr :
            if temp_arr[-1] == arr[j][h] :
                temp_arr.append(arr[j][h])
            else :
                break
            
    if(len(temp_arr)) == len(arr[j]):
        count += 1
    
print(count)