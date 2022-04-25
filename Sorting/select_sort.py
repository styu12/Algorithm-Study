# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복합니다.
# 시간복잡도: O(N^2) / 공간복잡도: O(N)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index = j
	# 반복문을 다 돌고나면 min_index에는 가장 작은 원소의 인덱스가 담긴다.
  array[i], array[min_index] = array[min_index], array[i]

print(array)
