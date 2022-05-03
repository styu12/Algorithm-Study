 
# 우선순위 큐
# - 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# - 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐 이용가능
# - Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 **표준 라이브러리 형태로 지원**함

# 힙
# - 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
# - **최소 힙(Min Heap)과 최대 힘(Max Heap)**이 있음
# - 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됨


# 파이썬 힙 라이브러리는 기본적으로 min Heap 제공
import heapq

def heapsort(iterable):
  h = []
  result = []

  for value in iterable:
    heapq.heappush(h, value)

  for i in range(len(h)):
     result.append(heapq.heappop(h))

  return result


result = heapsort([1,5,3,4,9,26,0,8,2])
print(result)

# max Heap 사용하고 싶으면, - 부호 붙여서 넣고, 꺼낼때도 - 부호 붙여서 꺼내자
import heapq

def heapsort(iterable):
  h = []
  result = []

  for value in iterable:
    heapq.heappush(h, -value)

  for i in range(len(h)):
     result.append(-heapq.heappop(h))

  return result


result = heapsort([1,5,3,4,9,26,0,8,2])
print(result)