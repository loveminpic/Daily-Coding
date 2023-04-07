question1, question2 = map(str,input().split())
answer1 = ""
answer2 = ""

for i in range(2,-1,-1) :
    answer1 += question1[i]
    answer2 += question2[i]

if int(answer1) > int(answer2) :
    print(answer1)
else :
    print(answer2)