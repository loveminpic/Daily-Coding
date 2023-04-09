num = int(input())

for i in range(0, num) :
    temp = input()
    temp_len = len(temp)
    zero = 0
    result = 0
    for i in range(0, temp_len) :
        if temp[i] == "O" :
            zero += 1
            result += zero
        else :
            zero = 0
    
    print(result)