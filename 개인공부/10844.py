import sys

n = int(sys.stdin.readline())

dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
    
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)


# arr = []
# arr.append(0)
# arr.append(9)

# if N == 1 :
#     print(arr[N])
    
# count = 1

# for i in range(2, N+1) :
#     temp = (arr[i-1] * 2) - count
#     arr.append(temp)
#     count += 1

# print(arr)

# print(arr[N]%1000000000)

# arr = {}
# if N > 1 :
#     start = 10**(N-1)
#     end = (10**N)-1
# else :
#     start = 1
#     end = 9

# m = str(start)

# check = True
# for i in range(len(m)- 1):
#     if abs(int(m[i]) - int(m[i+1])) != 1 :
#         check = False
#         break
    
# if check == True :
#     arr[start] = 1
# else :
#     arr[start] = 0

# for i in range(start+1, end+1) :
#     arr[i] = 0
#     check = True
#     temp = str(i)
#     for j in range(len(temp) - 1) :
#         if (abs(int(temp[j]) - int(temp[j+1])) != 1) :
#             check = False
#             break
#     if check == True :
#         arr[i] = arr[i-1] + 1
#     else :
#         arr[i] = arr[i-1]

# print(arr)





