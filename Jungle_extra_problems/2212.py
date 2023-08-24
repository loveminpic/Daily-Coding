import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())

sensor = sorted(list(map(int, input().split())))

result = []
if K >= N:
    print(0)

else:
    for i in range(1, len(sensor)):
        result.append(abs(sensor[i] - sensor[i - 1]))

    result = sorted(result)

    for i in range(K - 1):
        result.pop()

    print(sum(result))
