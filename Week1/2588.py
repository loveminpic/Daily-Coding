A = input()
B = input()

len_b = len(B)
for i in reversed(range(len_b)):
    print(int(A) * int(B[i]))
print(int(A)*int(B))