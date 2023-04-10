# index 화살표가 두개 필요하고
# 피봇 설정이 필요함

def quicksort(list) :
    check_len = len(list)
    one = 0
    two = 0
    pivot = check_len - 1
    for i in range(0,check_len) :
        if two == check_len-1 :
            list[one], list[pivot] = list[pivot], list[one]
            quicksort(list[0,-1])
        elif list[two] < list[pivot] :
            list[one], list[two] = list[two], list[one]
            one, two+=1
        else :
            two+=1    
            