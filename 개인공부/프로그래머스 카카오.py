def solution(cacheSize, cities):
    answer = 0
    cacheList = {}

    index = 0

    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cacheList:
            answer += 1
            cacheList[city] = index
        else:
            if len(cacheList) == 0:
                cacheList[city] = index
                answer += 5
            else:
                if len(cacheList) < cacheSize:
                    cacheList[city] = index
                    answer += 5
                else:
                    min_num = 1000000
                    min_city = ""
                    for key in cacheList.keys():
                        if min_num > cacheList[key]:
                            min_city = key
                            min_num = cacheList[key]
                    del cacheList[min_city]
                    cacheList[city] = index
                    answer += 5
        index += 1
    return answer


print(
    solution(
        5,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
)
