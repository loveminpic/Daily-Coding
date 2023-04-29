import sys

case = int(sys.stdin.readline().strip())

for j in range(0, case):
    people = int(sys.stdin.readline().strip())

    score = []


    for i in range(0,people) :
        score.append(list(map(int, sys.stdin.readline().split())))

    score.sort(key=lambda x : (x[0], x[1]))
    count = 1
    first = score[0][0]
    second = score[0][1]
    
    for h in range(1,len(score)) :
        if first > score[h][0] or second > score[h][1]:
            if first > score[h][0] :
                first = score[h][0] 
            if second > score[h][1] :
                second = score[h][1] 
            count += 1 
            
    print(count)