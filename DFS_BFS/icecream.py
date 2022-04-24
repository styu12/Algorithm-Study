# 아이스크림 얼려먹기 문제
# 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1, 0끼리 연결되어 있는 부분은 하나의 아이스크림으로 얼려진다. -> 아이스크림의 개수는?

def dfs(x, y):
  if x <= -1 or x >= m or y <= -1 or y >= n:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

m, n = map(int,input().split())

graph = []
for i in range(m):
  graph.append(list(map(int, input().split())))

result = 0
for i in range(m):
  for j in range(n):
    if dfs(i, j):
      result += 1

print(result)