import sys

input = sys.stdin.readline

N, M = map(int, input().split())
recode = list(map(int,input().split()))

diff = 1000000000
temp = 0
div = N//M
length_div = list(div for _ in range(M))
left = N-sum(length_div)
for i in range(left) :
    length_div[i] += 1

# 최소와 최대의 차이가 커질때 break
while diff :
    
    result = []
    start  = 0
    end = 0
    
    for i in range(0,M) :
        end += length_div[i]
        result.append(sum(recode[start:end]))
        start = end
        
    mi = min(result)
    mx = max(result)
    
    min_index = result.index(mi)
    max_index = result.index(mx)
    
    if abs(mx-mi) >= diff and temp <= mx:
        break
    
    temp = mx
    diff = abs(mx-mi)
    
    
    length_div[min_index] += 1
    length_div[max_index] -= 1    
    
print(temp)
    

