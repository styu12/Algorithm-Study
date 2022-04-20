## 문자열을 입력받은 후 알파벳은 순서대로 정렬, 숫자는 합쳐서 마지막에 붙이기

data = input()
sum = 0
list = []

for x in data:
  if x.isalpha():
    list.append(x)
  else:
    sum += int(x)

list.sort()
if sum != 0:
  list.append(str(sum))

print("".join(list))