# 통로를 통해 1. 몇 개의 도시에 메세지를 보낼 수 있는지, 2. 모든 도시가 다 메세지를 받는 데 걸리는 시간 구하기

import heapq
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[]] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = distance[now] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
  if d == INF or d == 0:
    continue
  else:
    count += 1
    max_distance = max(max_distance, d)

print(count, max_distance)