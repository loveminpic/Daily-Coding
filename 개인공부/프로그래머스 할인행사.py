import copy


def solution(want, number, discount):
    answer = 0
    dic = {}

    for i in range(len(want)):
        dic[want[i]] = number[i]

    while len(discount) >= 10:
        temp = copy.deepcopy(discount[0:10])
        temp2 = copy.deepcopy(dic)
        mx = sum(number)

        for key in temp2:
            value = temp2[key]

            for i in range(value):
                if key in temp:
                    temp.remove(key)
                    x -= 1
                    mx -= 1

                else:
                    break
        if mx == 0:
            answer += 1
        if len(discount) != 0:
            discount.pop(0)
    return answer


print(
    solution(
        ["apple"],
        [10],
        [
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
        ],
    )
)
