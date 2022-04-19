## 공포도가 3인 사람은 3명 이상의 그룹에만 들어갈 수 있어 => 공포도를 보면서 만들 수 있는 그룹의 최댓값을 구해보자

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
member = 0
for i in data:
  member += 1
  if member >= i:
    result += 1
    member = 0

print(result)
