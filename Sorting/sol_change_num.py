# 두 배열의 원소 교체문제
# k번의 교체 가능횟수가 있다. => b에서 큰 수가 있다면 교체해서 a로 가져온다.
# a 원소들의 합이 최대가 되게 만들어서 최댓값을 출력한다.
# a는 오름차순 정렬, b는 내림차순 정렬한 뒤 동일 인덱스로 동시에 반복문 돌리는 게 포인트

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 배열 A는 오름차순 정렬
b.sort(reverse=True) # 배열 B는 내림차순 정렬

# 같은 인덱스를 활용하며 최대 k번째까지 a와 b 동시 체크
for i in range(k):
  # A의 원소가 B의 원소보다 작은 경우
  if a[i] < b[i]:
    # 두 원소를 교체
    a[i], b[i] = b[i], a[i]
  else: # 그렇지 않으면 반복문 탈출
    break

print(sum(a))