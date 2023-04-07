x,y,w,h = map(int, input().split())

if w-x < x - 0 :
    min = w-x
else :
    min = x - 0
    
if h-y < y - 0 :
    min2 = h-y
else :
    min2 = y - 0
    
if min <= min2 :
    print(min)
else :
    print(min2)
