import sys

input = sys.stdin.readline

N,M = map(int,input().split())
dic = {}

for i in range(N):
    temp = input().strip()
    
    if len(temp) >= M :
        if temp in dic :
            dic[temp] += 1
        else :
            dic[temp] = 0

dic = dict(sorted(dic.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

for i in dic.keys() :
    print(i)