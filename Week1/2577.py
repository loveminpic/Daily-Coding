result = [0 for i in range(10)]

a = int(input())
b = int(input())
c = int(input())

total = list(map(int, str(a*b*c)))
len_total = len(total)

for i in range(0, len_total) :
    m = int(total[i])
    result[m] += 1

for j in range(0, len(result)) :
    print(result[j])