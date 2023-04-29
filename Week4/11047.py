import sys

coin, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(0,coin) :
    coins.append(int(sys.stdin.readline().strip()))
    
coins.sort(reverse=True)

count = 0
while k > 0 :
    for i in range(0,coin) :
        if coins[i] <= k :
            count += k // coins[i]
            k = k % coins[i]
print(count)