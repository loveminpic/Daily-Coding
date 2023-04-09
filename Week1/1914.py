def move(n, start, end) :
    mid = 6 - start - end
    
    if n == 1 :
        print(start, end)
        
    elif n >=2 :
        move(n-1, start, mid)
        move(1, start, end)
        move(n-1, mid, end)
        
def move2(n, start, end) :
    mid = 6 - start - end

    if n >=2 :
        move2(n-1, start, mid) 
        move2(1, start, end)
        move2(n-1, mid, end)
        
a = int(input())
print((2**a)-1)

if a <= 20 :
    move(a,1,3) 