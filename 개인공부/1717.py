import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [set([i] for i in range(n+1))]


for i in range(m) :
    check = False
    a,b,c = map(int, input().split())
    
    temp1 = -1
    temp2 = -1
    
    if( a == 0 ) :
        for j in range(len(arr)) :
            if temp1 >= 0 and temp2 >= 0 :
                break
            if b in arr[j] :
                temp1 = j
            if c in arr[j] :
                temp2 = j
        for h in range(len(arr[temp2])) :
            arr[temp1].append(arr[temp2][h])
        if b != c :
            del arr[temp2]
    else :
        for j in range(len(arr)) :
            if b in arr[j] :
                if c not in arr[j] :
                    break
                else :
                    check = True
                    break
            if c in arr[j] :
                if b not in arr[j]:
                    break
                else :
                    check = True
                    break
                
        if check == False :
            print("NO")
        else :
            print("YES")
            