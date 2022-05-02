## 식량창고는 최소한 한 칸 이상 떨어져있어야 개미전사가 식량을 털 수 있다.
## 최대로 가져올 수 있는 식량 양은?

## => 점화식을 잘 활용하자!!

n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
  d[i] = max(d[i-1], d[i-2]+arr[i])

print(d[-1]) 