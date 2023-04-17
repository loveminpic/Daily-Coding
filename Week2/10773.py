import sys

num = int(sys.stdin.readline().strip())

stack = []
for i in range(0, num) :
    
    n = int(sys.stdin.readline().strip())
    
    if n == 0 :
        stack.pop()
    else :
        stack.append(n)
        
print(sum(stack))

