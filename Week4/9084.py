import sys
input = sys.stdin.readline

num = int(input().strip())

for i in range(0,num) :
    coin_num = int(input().strip())
    coin = list(map(int, input().split()))
    value = int(input().strip())
    arr = [0] * (value + 1)
    arr[0] = 1
    
    for h in range(0, coin_num) :
        for j in range(1, value + 1):
            if j >= coin[h] :
                arr[j] += arr[j-coin[h]]
    print(arr[value])