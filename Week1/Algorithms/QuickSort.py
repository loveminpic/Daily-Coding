
def quicksort(list, left, right) :
    p_left = left
    p_right = right
    pivot = list[left+right//2]
    
    while p_left <= p_right :
        while list[p_left] < pivot :
            p_left += 1
        while list[p_right] > pivot :
            p_right -= 1    
        if p_left <= p_right :
            list[p_left], list[p_right] = list[p_right], list[p_left]
            p_left += 1
            p_right -= 1  
        
    if left < p_right : 
        quicksort(list, left, p_right)
    if p_left < right :
        quicksort(list, p_left, right)
                    

