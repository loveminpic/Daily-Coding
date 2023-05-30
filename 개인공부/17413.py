import sys

input = sys.stdin.readline


arr = input().strip()
result = []
check = False
temp = ""
for i in range(len(arr)) :
    if arr[i] == "<" :
        check = True
        if temp != "" :
            temp = temp[::-1]
            result.append(temp)
            temp = ""
        temp += arr[i]
    elif arr[i] == ">" :
        temp += arr[i]
        result.append(temp)
        temp = ""
        check = False
    elif arr[i] == " " :
        if check == True :
            temp += arr[i]
        else : 
            if temp != "" :
                temp = temp[::-1]
                result.append(temp)
                temp = ""
            result.append(arr[i])
    else :
       temp += arr[i]
            

if temp != "" :
    temp = temp[::-1]
    result.append(temp)


final = ""
for i in result :
    final+= i
    
print(final)