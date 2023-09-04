import sys

N = int(sys.stdin.readline().strip())


def find_sosu(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return False
    return True


for i in range(N, 1000000**2):
    result = True
    if find_sosu(i) == True:
        temp = str(i)
        temp2 = []
        for j in range(len(temp)):
            temp2.append(temp[j])

        for h in range(len(temp2) // 2):
            temp3 = temp2.pop()
            if temp2[h] != temp3:
                result = False
                break

        if result == True:
            print(i)
            break
