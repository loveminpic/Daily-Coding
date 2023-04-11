list = [5,4,3,2,1]
print("list :" , list)

list.sort()
print("sort(): ",list)

list = [5,4,3,2,1] # 다시 5,4,3,2,1로 list로 만든 후
list2 = sorted(list) # sorted(list) 실행
print("sorted after list : ", list) # 원래 리스트는 변화 없고
print(list2) # sorted(list)를 담은 list2 는 변화 
