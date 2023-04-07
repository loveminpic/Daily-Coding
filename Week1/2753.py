# 4의 배수이면서 100의 배수가 아닐때 또는 400 배수일때, 

def year_check(num): 
    if num % 4 == 0  and num % 100 > 0:
        print("1")
    elif num % 400  == 0 :
        print("1") 
    else :
        print("0")

year = int(input())
year_check(year)