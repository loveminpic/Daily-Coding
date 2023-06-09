import sys

N =int(sys.stdin.readline().strip())

for i in range(N) :
    A, B = map(int, sys.stdin.readline().split())

    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))
    count = 0
    
    a_list = sorted(a_list,reverse=True)
    b_list = sorted(b_list)
    
    a_len = len(a_list)
    b_len = len(b_list)
    
    for j in range(a_len) :
        for g in range(b_len) :
            if b_list[g] < a_list[j] :
                count += 1
            else :
                break

    print(count)