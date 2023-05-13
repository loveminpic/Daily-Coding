import sys
input = sys.stdin.readline
a, b = map(int,input().split())
x = {}

for i in range(a):
    x[input().strip()] = 1

result = []

for i in range(b):
    temp = input().strip()    
    if temp in x :
        result.append(temp)
    
print(len(result))
result.sort()         
for j in result :
    print(j)
    
    
    
    