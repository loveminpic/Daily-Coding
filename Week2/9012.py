import sys 

num = int(sys.stdin.readline().strip())

for i in range(0, num) :
    
    s = str(sys.stdin.readline())
    stack = []
    
    for h in range(0, len(s)-1) :
        stack.append(s[h])
        
    
    stack2 = []
    
    for j in range(0, len(stack)) :
        if(stack[j] == '(') :
            stack2.append('(')
        else :
            if len(stack2) != 0 and stack2[-1] == '(' :
                stack2.pop()
            else :
                stack2.append(-1)
    
    if len(stack2) == 0 :
        print('YES')
        
    else :
        print("NO")