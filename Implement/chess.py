
## 체스판 나이트가 움직일 수 있는 경우의 수 구하기

pos = input()
x = int(pos[1])
y = ord(pos[0]) - ord('a') + 1
count = 0

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

for step in steps:
  nx = x + step[0]
  ny = y + step[1]
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  count += 1

print(count)