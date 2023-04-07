a,b = map(int, input().split())
list_zero = [[0,b]]
list_one = [[1,a]]

num = int(input())

for i in range(0, num) :
    c,d = map(int, input().split())
    if(c == 0) : 
        list_zero.append([c,d])
    else :
        list_one.append([c,d])
        
list_zero.sort()
list_one.sort()

max_zero = 0
temp = 0
max_one = 0

for i in range(0,len(list_zero)) :
    if max_zero < abs(temp - list_zero[i][1]) :
        max_zero = abs(temp - list_zero[i][1])
        temp = list_zero[i][1]
    else :
        temp = list_zero[i][1]

temp = 0

for i in range(0,len(list_one)) :
    if max_one < abs(temp - list_one[i][1]) :
        max_one = abs(temp - list_one[i][1])
        temp = list_one[i][1]
    else :
        temp = list_one[i][1]    

print(max_one * max_zero)
        
    
