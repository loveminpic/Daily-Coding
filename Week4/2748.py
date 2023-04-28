import sys
arr = [0] * 100

def fibo(num) :
    if num <= 2 :
        return 1
    if arr[num] != 0 :
        return arr[num]
    arr[num] = fibo(num-1) + fibo(num-2)
    return arr[num]

num = int(sys.stdin.readline().strip())

print(fibo(num))