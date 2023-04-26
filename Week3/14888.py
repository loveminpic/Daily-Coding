import sys
import collections

input = sys.stdin.readline

def dfs(index, stack) :
    global operator2
    stack.append(index)
    if len(operator2) == 0 :
        return stack
    m = operator2.popleft()
    stack.append(m)
    for i in nodes[index] :
        stack = dfs(i, stack)
        operator2.append(m)
    return stack

def calculate(stack):
    while len(stack) > 1:
        num1 = stack.pop(0)
        operator = stack.pop(0)
        num2 = stack.pop(0)

        if operator == '+':
            result = num1 + num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '/':
            if num1 < 0 and num2 > 0:
                num1 = abs(num1)
                result = -(num1 // num2)
            else:
                result = num1 // num2
        stack.insert(0, result)

    return stack[0]

num = input().split()

temp = list(map(int,input().split()))
operator2 = collections.deque()
operator = list(map(int, input().split()))

for i in range(0, len(operator)) :
    ops = operator[i]
    if i == 0 :
        m = '+'
    elif i == 1 :
        m = '-'
    elif i == 2 :
        m = '*'
    elif i == 3 :
        m = '/'
    for j in range(0,ops) :
        operator2.append(m)
        
mx = max(temp)
nodes = [[] * (mx +1) for i in range (mx+1)]

for i in range(0,len(temp)-1):
        nodes[temp[i]].append(temp[i+1])

result = []
for i in range(0,len(operator2)) :
    stack = []
    stack = dfs(temp[0], stack)
    result.append(calculate(stack))
    
print(max(result))
print(min(result))