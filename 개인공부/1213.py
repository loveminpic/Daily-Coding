import sys

str_name_arr = sys.stdin.readline().strip()
str_name = set(str_name_arr)
uni = str_name.union()
dict_name = {}

for i in uni :
    dict_name[i] = 0

for i in range(len(str_name_arr)) :
    for j in dict_name.keys() :
        if str_name_arr[i] == j :
            dict_name[j] += 1

reuslt = []
left = {}
dict_name = dict(sorted(dict_name.items()))


for key, value in dict_name.items() :
    if (value % 2 == 0) :
        for j in range(value//2) :
            reuslt.append(key)
    else :
        for j in range(value//2):
            reuslt.append(key)
        left[key] = 1

temp = reuslt[::-1]

if len(left) > 1 : 
    print("I'm Sorry Hansoo")
else : 
    for key, value in left.items() :
        for i in range(value) :
            reuslt.append(key)

    for i in temp :
        reuslt.append(i)

    for i in reuslt :
        print(i, end ='')
