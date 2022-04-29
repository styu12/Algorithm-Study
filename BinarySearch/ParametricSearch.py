# 떡볶이 떡 만들기 문제 - 떡이 여러 개 있고 자르는 기계는 전부 똑같은 길이로만 자를 수 있음
# ex. 19, 14, 10, 17 => 15로 자르면? => 4, 2 => 6만큼 손님이 가져가는 것
# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 문제

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
  total = 0
  mid = (start + end) // 2

  for x in array:
    if x > mid:
      total += (x-mid)

  if total < m:
    end = mid - 1
  else: 
    result = mid
    start = mid + 1

print(result)