def find_order(n, r, c):
    if n == 0:
        return 0
    
    size = 2 ** (n-1)
    part_size = size ** 2
    part = 0
    
    if r < size and c < size:
        part = 0
    elif r < size and c >= size:
        part = 1
        c -= size
    elif r >= size and c < size:
        part = 2
        r -= size
    else:
        part = 3
        r -= size
        c -= size
    return part_size * part + find_order(n-1, r, c)


n, r, c = map(int, input().split())
print(find_order(n, r, c))