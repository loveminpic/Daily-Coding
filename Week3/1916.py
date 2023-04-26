import sys
import collections
input = sys.stdin.readline

city_num = int(input().strip())
line = int(input().strip())

price_node = [[] for i in range(0, city_num+1)]
 
for i in range(0, line) :
    a,b,c = map(int,input().split())
    price_node[a].append((b,c))
        
start, end = map(int,input().split())

min_price = [float('inf')] * (city_num + 1)
min_price[start] = 0
visited = [False] * (city_num + 1)

for _ in range(city_num):
    min_val = float('inf')
    current_city = -1

    # 아직 방문하지 않은 도시 중 최소 비용을 가진 도시 찾기
    for i in range(1, city_num + 1):
        if visited[i] == False and min_val > min_price[i]:
            min_val = min_price[i]
            current_city = i
    
    visited[current_city] = True  # 선택한 도시를 방문 처리
    
    # 선택한 도시를 기준으로 이웃 도시들의 비용 업데이트
    for next_city, cost in price_node[current_city]:
        if min_price[next_city] > min_price[current_city] + cost:
            min_price[next_city] = min_price[current_city] + cost
            
print(min_price[end])