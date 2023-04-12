import sys

n = int(input())
num = []
s = [[] for _ in range(51)]
    
for i in range(0, n) :
    num.append(input())
    

num = list(set(num))

num.sort()


for i in range(0, len(num)) :
    check_len = len(num[i])
    s[check_len].append(num[i])
     
for i in range(0, len(s)) :
    for j in range(0,len(s[i])) :
        if len(s[i]) == 0 :
            pass
        else :
            print(s[i][j])
  