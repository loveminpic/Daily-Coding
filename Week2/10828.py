import sys

num = int(sys.stdin.readline().strip())
stack = []
function_name = []

for i in range(0,num) :

    function_name = sys.stdin.readline().split()
    
    if function_name[0] == "push" :
        stack.append(int(function_name[1]))
        
    elif function_name[0] == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
            stack.pop()
            
    elif function_name[0] == "size" :
        print(len(stack))
        
    elif function_name[0] == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
            
    elif function_name[0] == "top" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
        
