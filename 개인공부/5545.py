import sys
import math
input = sys.stdin.readline

topping_num = int(input().strip())
dow_price, topping_price = map(int, input().split())

dow_cal = int(input().strip())
topping_cal = []

for i in range(topping_num) :
    topping_cal.append(int(input().strip()))
    
topping_cal = sorted(topping_cal, reverse=True)
result = []


result.append(dow_cal//dow_price)

for i in range(1,topping_num+1):
    temp = 0
    for j in range(0,i) :
        temp += topping_cal[j]
    result.append((dow_cal + temp) // (dow_price + (topping_price * i)))
    
print(max(result))

