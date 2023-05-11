import sys

input = sys.stdin.readline

num = int(input().strip())
x = []
dp = [[0] * 101 for i in range(101)]
count = 0

for i in range(num):
    a, b = map(int,input().split())
    for j in range(a, a+10):   
        for h in range(b, b+10):   
            if dp[j][h] != 1 :
                dp[j][h] = 1
                count+= 1

 
print(count)

