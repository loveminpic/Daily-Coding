import sys

n_num = int(input()) 
N = list(map(int,sys.stdin.readline().split()))

m_num = int(input())
M = list(map(int,sys.stdin.readline().split()))

N.sort()
check = False 

def find_number_in(m,start, end):
    global check
    half = abs(start - end) // 2
    
    if m < N[half+start] :
        if half == 0 :
            return check
        find_number_in(m, start , half+start)
    elif m == N[half+start] :
        check = True
        return check
    else :
        if half == 0 :
            return check
        find_number_in(m ,half+start, end)
            
            
for i in range(0, m_num):
    check = False
    find_number_in(M[i],0,n_num)
    if check == True :
        print(1)
    else :
        print(0)
