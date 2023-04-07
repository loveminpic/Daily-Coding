a,b,v = map(int, input().split())
day_count = 0

day_count = (v-b) / (a-b)
if (v-b) % (a-b) != 0 :
    day_count+=1
    print(int(day_count))
else :
    print(int(day_count))
    
# while v > 0 :
#     day_count += 1
#     v -= a
#     if v <= 0 :
#         break
#     v += b
    
# print(day_count)