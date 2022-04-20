## 시간 1초씩 늘리면서 3이 있는 숫자는 체크하기

h = int(input())
count = 0

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)