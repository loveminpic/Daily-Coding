import sys

input = sys.stdin.readline
num = int(input().strip())
dance = set()

dance.add("ChongChong")

for i in range(num) :
    a, b = map(str,input().split())
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)
        
print(len(dance))