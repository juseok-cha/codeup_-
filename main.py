# 1356 : 사각형 출력하기 2


num = int(input())

for i in range(0,num):
  if i >= 1 and i <= num-2:
    print("*"+" "*(num-2)+"*")
  else:
    print(num*"*")
  



