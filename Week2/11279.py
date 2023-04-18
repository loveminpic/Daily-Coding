import sys
import collections 

def heapify(deque, n, i) :
    parents = i
    left = i * 2 + 1
    right = left + 1 
    
    if left < n and deque[parents] < deque[left] :
        parents = left
    
    if right < n and deque[parents] <  deque[right] :
        parents = right
    
    if i != parents :
        deque[i], deque[parents] =  deque[parents], deque[i]
        heapify(deque, n , parents)   
    

def heap_pop(dequeue) :
    
    temp = dequeue.pop()
    dequeue.appendleft(temp)
    heapify(dequeue, len(dequeue), 0)
    
def heap_push(dequeue):
    
    if len(dequeue) == 0 :
        return
    
    i = len(dequeue) - 1 
    
    while i > 0:
        parent = (i -1 )// 2 
        if dequeue[i] > dequeue[parent]:
            dequeue[parent], dequeue[i] = dequeue[i], dequeue[parent]
            i = parent
        else :
            break
        
    
num = int(sys.stdin.readline())
dequeue = collections.deque()

for i in range(0, num) :


    check = int(sys.stdin.readline())
    

    if check == 0 :
        if len(dequeue) != 0 :
            print(dequeue.popleft())
            if len(dequeue) != 0:
                heap_pop(dequeue)
        else :
            print(0)
    else :
        dequeue.append(check)

        heap_push(dequeue)
        
     