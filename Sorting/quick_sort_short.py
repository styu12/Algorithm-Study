# python의 list comprehension을 이용하면 훨씬 간결하게 작성 가능
# array 만들 때 조건문, 반복문 활용해서 간편하게 quick_sort를 구현하자
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))