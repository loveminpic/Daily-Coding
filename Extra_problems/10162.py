import sys

div = [60*5, 60, 10]
number = int(sys.stdin.readline().strip())
result = []

for i in range(3):
    result.append(number // div[i])
    number = number % div[i]

if number != 0:
    print(-1)
else:
    print(*result)
