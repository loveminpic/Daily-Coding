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
    result = [0,0]
    num2 = int(input())
    a = int(num2 / 2)
    b = int(num2 / 2)
    if a + b == num2 :
        if check(a) == True :
            result = [a, b]
        else :
            while result == [0,0] :
                a = a - 1
                b = b + 1
                if(a + b == num2) :
                    if check(a) == True and check(b) == True:
                        result = [a,b]
    print(result[0], result[1]) 
    
    