# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정합니다.
# 시간복잡도: O(NlogN)...최악의 경우 O(N^2)..계속 스위칭 못하고 끝까지 다 돌아야하니까 선형탐색 이중으로 하게됨. / 공간복잡도: O(N)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start
  left = start + 1
  right = end
  while(left <= right):
		# 피벗보다 큰 데이터 찾을 때까지 반복
		# pivot이 start니까 end까지 다 체크해야지 + left는 end 넘어가도 어차피 pivot이랑 바꿀 때 쓰이지 않는 인덱스라 상관 없어.
    while(left <= end and array[left] <= array[pivot]):
      left += 1
		# 피벗보다 작은 데이터 찾을 때까지 반복
		# pivot이 start니까 start는 체크할 필요 없어 + right은 pivot이랑 교체할 때 필요한 인덱스니까 0 밑으로 떨어지면 안돼
    while(right > start and array[right] > array[pivot]):
      right -= 1
    if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[pivot], array[right] = array[right], array[pivot]
    else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)