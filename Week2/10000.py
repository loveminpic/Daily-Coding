import sys

num = int(sys.stdin.readline().strip())
point = []

for i in range(0, num) :
    c, r = list(map(int,sys.stdin.readline().split()))
    point.append(["L", c - r])
    point.append(["R", c + r])

point.sort(key=lambda p: (-p[1], p[0]), reverse=True)

stack = []
area = 1

for curr in point :
    
    if curr[0] == "L" :
        stack.append(curr)
        continue
        
    cum_width = 0
    while stack :
        prev = stack.pop()
        
        if prev[0] == "C" :
            cum_width += prev[1]
            
        elif prev[0] == "L" :
            
            width = curr[1] - prev[1]
            
            if width == cum_width :
                area += 2
            else :
                area += 1
                
            stack.append(("C", width))
            break

print(area)

    