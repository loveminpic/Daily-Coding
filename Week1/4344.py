total = int(input())

for i in range(0, total) :
    students = list(map(int,input().split()))
    sum_list = (sum(students) - students[0]) / students[0]
    result = 0
    
    for j in range(1, students[0]+1) :
        if students[j] > sum_list :
            result += 1

    answer = result / students[0] * 100
    print("{:.3f}%".format(answer))