def heapify(arr, n,i):
    # 부모노드
    largest = i
    # 왼쪽 자식노드
    left = 2 * i + 1
    right = left + 1
    
     # 왼쪽 자식 노드가 존재하고, 현재 가장 큰 값보다 왼쪽 자식 노드의 값이 큰 경우
    if left < n and arr[largest] < arr[left] :  
        largest = left
    
     # 오른쪽 자식 노드가 존재하고, 현재 가장 큰 값보다 오른쪽 자식 노드의 값이 큰 경우
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 현재 노드가 가장 큰 값이 아니라면, 가장 큰 값과 현재 노드의 값을 교환하고 재귀적으로 heapify 함수를 호출합니다.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)    
        
        
def heap_sort(arr) :
    n = len(arr)
    
    for i in range(n //2 -1, -1, -1) :
        heapify(arr,n,i)
        
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
        
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)