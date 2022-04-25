# 한 칸씩 좌측 요소와 비교하면서 더 작으면 왼쪽으로 옮겨준다 생각하면 된다.
# 시간 복잡도: O(N^2) - 최선의 경우 O(N).. 이미 정렬되어 있을 때 / 공간복잡도 : O(N)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j-1]:
      array[j-1], array[j] = array[j], array[j-1]
    else:
      break

print(array)