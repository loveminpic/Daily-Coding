count = 0
num = int(input())
li = [0] * num

def bt(index) :
    global count, num, li
    if(index == num) :
        count += 1
        return
    
    else :
        for i in range(0, num) :
            li[index] = i
            check = True
            for j in range(index):
                if li[index] == li[j] or abs(index - j) == abs(li[index]- li[j]) :
                    check = False
                    break
            if check == True:
                bt(index+1)
    
bt(0)
print(count)