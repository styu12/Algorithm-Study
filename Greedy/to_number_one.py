# 1이 될 때 까지 빼거나 나누기

n, k = map(int, input().split())
count = 0

while True:
    if n < k:
        break
    target = (n // k) * k
    count += n - target
    n = target
    count += 1
    n //= k

count += (n-1)
print(count)