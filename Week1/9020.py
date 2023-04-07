def check(number) :
    if number == 1 or number == 0 :
        return False
    else :
        for i in range(2, int(number ** 0.5 + 1)) :
            if number % i == 0 :
                return False
    return True


num = int(input())
for i in range(num) :
    num2 = int(input())
    list = []
    result = []
    for j in range(num2) :
        if check(j) == True :
            list.append(j)
        else :
            pass

    for h in range(0, len(list)-1) :
        if list[h] * 2  == num2 :
            result = [list[h], list[h]]
        else :
            min = 100000
            for k in range(h+1,len(list)) :
                if list[h]+list[k] == num2 :
                    if min > list[k]-list[h] :
                        min = list[k]-list[h]
                        result = [list[h],list[k]]
                else :
                    pass
         
    print(result)
        