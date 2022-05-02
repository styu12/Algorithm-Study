## 효율적인 화폐구성 문제
## 화폐 종류에 따라 가장 효율적으로 특정 가격을 구성할 수 있는 최소의 화폐 개수 구하기

## 1원부터 m원까지 돌면서 각각 특정 코인만큼 뺐을 때의 dp값이랑 현재 dp값을 비교해서 작은 횟수로 갱신 - min()함수 활용
## 중간에 화폐 조합이 안되는 부분은 10001이라는 무한대값으로 표현.
## 이 짓을 각 코인마다 다 해주니까 결국에 가장 효율적인 구성 방법만 남음

n, m = map(int, input().split())
coins = []
d = [10001] * (m+1)

for i in range(n):
  coin = int(input())
  coins.append(coin)

# 다이나믹 프로그래밍 - 보텀업 방식 진행
d[0] = 0
for coin in coins:
  for j in range(coin, m+1):
    if d[j-coin] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j-coin]+1)

if d[m] == 10001:
  print(-1)
else: 
  print(d[m])