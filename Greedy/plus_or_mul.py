# 배열 돌면서 더하거나 곱해서 최대의 숫자 만들기

data = input()

result = int(data[0])

for i in range(1, len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)
    

  