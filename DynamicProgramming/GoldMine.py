## 금광 문제
## 오른쪽 위, 오른쪽, 오른쪽 아래 이렇게 세가지의 경로 선택지가 있음
## 각 칸에는 금이 들어있는데, 오른쪽으로 가면서 가장 최대로 얻을 수 있는 금의 양은?

## 2차원 배열 구성 => i번째 금칸 입장에서 이전의 경로를 보면 왼쪽 위/왼쪽/왼쪽 아래 이렇게 세 가지임
## 총 세 가지 경우 중 가장 max 값을 현재 금칸의 양에 더해주면서 갱신함 (물론 index 벗어날 때는 그냥 0으로 초기화해버리면서 오류 방지)
## 이제 맨 오른쪽 열에서 가장 큰 놈을 찾으면 최댓값 출력 가능

t = int(input())

for tc in range(t):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  d = []
  index = 0
  for i in range(n):
    d.append(array[index:index+m])
    index += m

  for j in range(1, m):
    for i in range(n):
			# 어차피 최댓값 구하는 것이니, index 벗어날 때는 0으로 초기화!
      if i == 0: leftup = 0
      else: leftup = d[i-1][j-1]

      if i == n-1: leftdown = 0
      else: leftdown = d[i+1][j-1]

      left = d[i][j-1]

			# 변수명을 직관적으로 하면 내가 생각하기에도 편하다.
      d[i][j] += max(leftup, left, leftdown)

	# result를 계속 갱신해나가는 방식
  result = 0
  for i in range(n):
    result = max(result, d[i][m-1])
  print(result)