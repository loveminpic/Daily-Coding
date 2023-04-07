
def check(num) :
    temp1 = int(num[0]) - int(num[1])
    temp2 = int(num[1]) - int(num[2])
    if temp1 == temp2 :
        return True
    else :
        return False


num = input()
result = 0

if int(num) < 100 :
    result = int(num)
else :
    for h in range(100, int(num)+1) : 
        num2 = str(h)
        if(num2[0]== num2[1]==num2[2]) :
            result+=1
            continue
        else :
            if check(num2) == True :
                result += 1
    result += 99
print(result)
