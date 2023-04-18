import sys
import collections

def infix_to_postfix (arr) :
    outstack = []
    opstack = []
    
    for i in range(0, len(arr)) :
        if arr[i] == "*" :
            if len(opstack) == 0  :
                 opstack.append(arr[i])
                 
            else :
                for j in range(len(opstack)-1, -1, -1) :
                    if opstack[j] == '/' :
                        outstack.append(opstack.pop())
                    else :
                        opstack.append(arr[i])
                        break
        elif arr[i] == "/" :
            if len(opstack) == 0  :
                 opstack.append(arr[i])
                 
            else :
                for j in range(len(opstack)-1, -1, -1) :
                    if opstack[j] == '*' :
                        outstack.append(opstack.pop())
                    else :
                        opstack.append(arr[i])
                        break
        elif arr[i] == '+' :
            if len(opstack) == 0  :
                 opstack.append(arr[i])
                 
            else :
                for j in range(len(opstack)-1, -1, -1) :
                    if opstack[j] == '*' or opstack[j] == '/' or opstack[j] == '-' :
                        outstack.append(opstack.pop())
                    else :
                        opstack.append(arr[i])
                        break
        elif arr[i] == '-' :
            if len(opstack) == 0  :
                 opstack.append(arr[i])
                 
            else :
                for j in range(len(opstack)-1, -1, -1) :
                    if opstack[j] == '*' or opstack[j] == '/' or opstack[j] == '+' :
                        outstack.append(opstack.pop())
                    else :
                        opstack.append(arr[i])
                        break
        elif arr[i] == "(" :
            opstack.append(arr[i])
        elif arr[i] == ")" :
            for h in range(len(opstack)-1, -1, -1 ):
                if opstack[h] == "(" :
                   opstack.pop()
                   break 
                else :
                    outstack.append(opstack.pop())
        else :
            outstack.append(arr[i])
        
        print("answer: ", outstack)
        print("opstack: ",opstack)    
    while len(opstack) != 0 :
        outstack.append(opstack.pop())
                    
    return outstack 


def calculate (arr) :
    arr2 = collections.deque()
    for i in arr :
        arr2.append(i)
        
    stack = []
    while len(arr2) != 0 :
        
        temp = arr2.popleft()
        
        if temp == "*" or temp == "/" or temp == "+" or temp == "-" :
            a = stack.pop()
            c = stack.pop()
            if temp == "*":
                stack.append(int(a) * int(c))
            elif temp == "/" :
                stack.append(int(c) / int(a))
            elif temp == "+" :
                stack.append(int(a) + int(c))
            elif temp == "-" :
                stack.append(int(a) - int(c))
        else :
            stack.append(temp)
        
        print(stack)
        if len(arr2) == 0 :
            break
        
    print(stack[0])


    

num = list(sys.stdin.readline().split())
temp = infix_to_postfix(num)
calculate(temp)
