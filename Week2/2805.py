import sys

num, need = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort(reverse=True)
start = 0
end = tree[0]
result = 0

while start <= end:
    count = 0
    half = (start + end) // 2

    for i in range(0, num):
        if tree[i] > half:
            count += tree[i] - half
        else:
            break

    if count < need:
        end = half - 1

    else:
        start = half + 1
        result = half


print(result)
