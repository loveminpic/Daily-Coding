import sys

N = int(sys.stdin.readline().strip())
tree = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    tree.append(temp)

for i in range(1, N):
    for j in range(len(tree[i])):
        if j == 0:
            tree[i][j] += tree[i - 1][j]
        elif j == len(tree[i]) - 1:
            tree[i][j] += tree[i - 1][j - 1]
        else:
            tree[i][j] += max(tree[i - 1][j - 1], tree[i - 1][j])

print(max(tree[N - 1]))
