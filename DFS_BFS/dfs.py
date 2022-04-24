# DFS - 깊이 우선으로 탐색하기! 

def dfs(graph, n, visited):
  visited[n] = True
  print(n, end=' ')
  for i in graph[n]:
    if not visited[i]:
      dfs(graph, i, visited)

	# 각 노드들의 인접 노드를 리스트로 정리해놓은 것
	# 1번부터 매칭하려고 0번 아이템은 비워놓자
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 여기도 마찬가지로 0번은 안 쓸거니까 9번째까지 생성
visited = [False] * 9
dfs(graph, 1, visited)