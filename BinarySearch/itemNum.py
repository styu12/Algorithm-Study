# 정렬된 배열에서 특정 수의 개수 구하기
# bisect 라이브러리 이용해서 손쉽게 구할 수 있음

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0 :
  print(-1)
else:
  print(count)