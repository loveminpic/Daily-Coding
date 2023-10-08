N, M = map(int, input().split())
orginal_town = [list(map(int, input().split())) for i in range(N)]
chicken_store_list = []
house_list = []

for i in range(N):
    for j in range(N):
        if orginal_town[i][j] == 2:
            chicken_store_list.append((i, j))
        if orginal_town[i][j] == 1:
            house_list.append((i, j))


def combination(arr, number):
    sorted(arr)
    combi_list = []

    def generate(start, chosen):
        if len(chosen) == number:
            combi_list.append(list(chosen))
            return

        for i in range(start, len(arr)):
            generate(i + 1, chosen + [arr[i]])

    generate(0, [])

    return combi_list


combi_list = combination(chicken_store_list, M)

result = [0 for _ in range(len(combi_list))]
count = -1

while len(combi_list) != 0:
    count += 1
    temp = combi_list.pop()

    for i, j in house_list:
        minimum = 1000000
        for tx, ty in temp:
            minimum = min(minimum, abs(tx - i) + abs(ty - j))
        result[count] += minimum

print(min(result))
