import sys

input = sys.stdin.readline

first = list(input().strip())
second = list(input().strip())

first.insert(0,0)
second.insert(0,0)

table = [[0] * (len(second)) for _ in range(0,len(first))]

for i in range(1, len(first)) :
    for j in range(1, len(second)) :
        if first[i] == second[j] :
            table[i][j] = table[i-1][j-1] + 1
        else :
            table[i][j] = max(table[i][j-1], table[i-1][j])

print(max(max(table)))
        