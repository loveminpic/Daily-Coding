import sys

input = sys.stdin.readline
N = int(input().strip())
n_list = list(map(int,input().split()))
dic = {}

for i in range(N) :
    if n_list[i] in dic :
        dic[n_list[i]] += 1
    else :
        dic[n_list[i]] = 1

M = int(input().strip())
m_list = list(map(int,input().split()))


for i in range(M) :
    if m_list[i] in dic :
        print(dic[m_list[i]], end=' ')
    else :
        print(0, end=' ')