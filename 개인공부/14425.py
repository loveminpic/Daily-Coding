import sys

input = sys.stdin.readline

N, M  = map(int,input().split())

n_arr = {}
m_arr = {}

for i in range(N):
    n_arr[(input().strip())] = 0
    
count = 0

for i in range(M):
    temp = input().strip()
    m_arr[temp] = 0 
    if temp in n_arr :
        count += 1
        
print(count)