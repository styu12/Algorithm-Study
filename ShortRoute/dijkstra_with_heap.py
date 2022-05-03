# - 단계마다 방문하지 않은 노드 중 최단거리가 가장 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용
# - 다익스트라 알고리즘이 동작하는 기본 원리는 동일
#     - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다른 것
#     - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값을 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보를 입력받기
for _ in range(m):
  a, b, c = map(int,input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q: #큐가 비어있지 않다면
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들 확인
    for i in graph[now]:
      cost = distance[now] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) 

#다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
  # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
  if distance[i] == INF:
    print("INFINITY")
  # 도달할 수 있는 경우, 거리를 출력
  else:
    print(distance[i])