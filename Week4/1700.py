import sys
input = sys.stdin.readline

N, K = map(int, input().split())
item = list(map(int, input().split()))

multitab = []
count = 0

for i in range(len(item)):
    if item[i] in multitab:
        continue

    if len(multitab) < N:
        multitab.append(item[i])
    else:
        out_idx = 0
        max_future = 0

        for j in range(len(multitab)):
            if multitab[j] not in item[i+1:]:
                out_idx = j
                break
            else:
                future_usage = item[i + 1:].index(multitab[j])
                if future_usage > max_future:
                    max_future = future_usage
                    out_idx = j

        multitab[out_idx] = item[i]
        count += 1

print(count)
