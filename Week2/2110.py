import sys

house_num, wifi = map(int, sys.stdin.readline().split())
house_location =[int(sys.stdin.readline().strip()) for i in range(0,house_num)]

house_location.sort()
mx = house_location[house_num-1]

start = 0
end = mx

if house_num == wifi :
    li = []
    for i in range(0, house_num-1) :
        li.append(house_location[i+1] - house_location[i])
    print(min(li))

else :
    while start <= end :
        
        distance = (start + end ) // 2
        count_house = 1
        last_house = house_location[0]
        
        for i in range(1,house_num) :
            if last_house + distance <= house_location[i] :
                count_house +=1
                last_house = house_location[i]
                if count_house > wifi :  
                    break

        if count_house < wifi :
            end = distance - 1
        
        else  :
            start = distance + 1
            result = distance
            

    print(result)