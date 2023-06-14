import sys
import math

N = int(sys.stdin.readline().strip())

if N == 1 :
    start = 2
    end = 7
else :
    start = 2 * (10 ** (N-1))
    end = (1 * (10 ** (N)) -1) - (2* (10 **(N-1)))

def check (n) :

    for i in range(2,int(math.sqrt(n) + 1)) :
        if n % i  == 0 :
            return False
    return True

while start != end :
    temp = str(start)
    result = True
 
    for h in range(1, N+1) :
        m = check(int(temp[0:h]))
        if m == False :
            result = False         
            break

    if result == True :
        print(start)
                   
    start += 1
    temp2 = str(start)
    if(temp2[0] == '4' or temp2[0]== '6') :
        start += 10**(N-1)
   