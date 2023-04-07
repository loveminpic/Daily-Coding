num = int(input())

for i in range(0, num) :
    word = ""
    chr_num = list(map(str, input().split()))
    
    for j in range(0, len(chr_num[1])) :
        for h in range(int(chr_num[0])) :
            word += chr_num[1][j]
    print(word)