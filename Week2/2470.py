import sys

num = int(sys.stdin.readline().strip())
liq = list(map(int,sys.stdin.readline().split()))

liq.sort()
start = 0
end = num
turn = 1000000
temp = num-1

while start <= end :

   mid = (start + end) // 2
    
   if liq[mid] > 0 :
       if turn > liq[mid] - 0 :
            turn = liq[mid] - 0
            temp = mid
            end = mid - 1
       else :
            break
        
   elif liq[mid] < 0 :
       if turn > 0 - liq[mid] :
            turn = 0 - liq[mid]
            temp = mid
            start = mid + 1
       else :
           break

   else :
       temp = mid
       break

mid = liq[temp]

a = abs(liq[temp] + liq[temp+1])
b = abs(liq[temp-1] + liq[temp])
c = abs(liq[0] + liq[num-1])

if a < b:
    if a < c :
        print(liq[temp] ,liq[temp+1])
    else :
        print(liq[0] , liq[num-1])
else :
    if b < c :
        print(liq[temp-1] , liq[temp])
    else :
        print(liq[0] , liq[num-1])



# if liq[temp] <= 0 :
#     if abs(liq[temp] + liq[temp+1]) > abs(liq[0] + liq[num-1]) :
#         print(liq[0], liq[num-1])
#     else :
#         print(liq[temp],liq[temp+1])
# else :
#     if abs(liq[temp] + liq[temp-1]) > abs(liq[0] + liq[num-1]) :
#         print(liq[0], liq[num-1])
#     else :
#         print(liq[temp], liq[temp-1])
   