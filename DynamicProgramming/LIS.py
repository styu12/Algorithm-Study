## 병사 배치 문제
## 공격력 높은 순으로 나열하고 싶다 (무조건 앞에 애가 더 쎄야 함)
## 병사를 열외시키는 방식으로 할 건데, 열외병사의 최솟값을 출력해라

## LIS (Longest Increasing Subsequences) 를 활용하자
## 반대 개념이니 병사 배열을 거꾸로 한 뒤에 적용하면 돼 
## i번째 dp는 i번째 아이템을 끝으로 한 배열의 길이! 
## 그럼, i번째 dp는 0 ~ i-1번째의 아이템들을 보면서 i번째 아이템보다 작다면! d[i] vs d[j]+1 둘 중 최댓값으로 dp를 갱신하면
## 각 아이템을 끝으로 하는 배열들 중 길이가 가장 긴 애들만 남겠지
## 그 길이들 중 최댓값을 고르면 가장 긴 배열이지 => 그 길이를 원래 길이에서 빼면 "열외 병사의 수!"

n = int(input())
array = list(map(int, input().split()))
# 이거는 내림차순 문제를 원하니까 array를 reverse해서 동일하게 접근하자
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n 

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
  for j in range(i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))