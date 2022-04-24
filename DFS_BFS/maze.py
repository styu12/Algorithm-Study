from collections import deque

# 미로 탈출 문제
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1 => (1,1) 에서 (n,m)까지 괴물을 피해 갈 수 있는 최단경로의 길이는? (출발시, 도착시 모두 +1 한다.)

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
  return graph[n-1][m-1]

print(bfs(0,0))