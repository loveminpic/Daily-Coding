import sys

num = int(sys.stdin.readline().strip())
time_table = []

for i in range(0, num) :
    time_table.append(list(map(int,sys.stdin.readline().split())))

time_table.sort(key=lambda x : (x[1], x[0]))


end_time = 0
count = 0

for start, end in time_table:
    if start >= end_time:
        count += 1
        end_time = end

print(count)