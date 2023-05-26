import sys
input = sys.stdin.readline

need, brand = map(int, input().split())
temp = need // 6 
temp2 = need % 6

min_key = 1000000
min_val = 1000000
mi = 100000000

for i in range(brand) :
    a, b = map(int,input().split())
    if min_key > a :
        min_key = a
    if min_val > b :
        min_val = b

if temp2 == 0 :
    if mi > min_key * temp :
        mi = min_key * temp
    if mi > min_val * need :
        mi = min_val * need
else :
    if mi > min_key * (temp+1) :
        mi = min_key * (temp+1)
    if mi > min_val * need :
        mi = min_val * need
    if mi > (min_key * temp) + (min_val * temp2) :
        mi = (min_key * temp) + (min_val * temp2)

print(mi)
    