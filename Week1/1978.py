num = int(input())
num_list = list(map(int,input().split()))
count = 0

for i in range(0, num) :
    check = True
    if num_list[i] == 1 :
        check = False
    elif num_list[i] == 2 :
        pass
    else :
        for j in range(2, num_list[i]) :
            if num_list[i] % j == 0 :
                check = False
            else :
                pass
    if check == True :
            count += 1
print(count)
