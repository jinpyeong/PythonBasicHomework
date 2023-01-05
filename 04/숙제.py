# 1
a,b


# 2
T
F
F
T
T
F
T


# 3
T
T
F
T
T
T


# 4
코딩


# 5
1,3,5


# 6
user = input("")
if user:
    print("짝수")
else:
    print("홀수")


# 7
num1 = int(input("input number1: "))
num2 = int(input("input number2: "))
num3 = int(input("input number3: "))
big = 0

if num1 > num2 and num1 > num3:
  big = num1
elif num2 > num1 and num2 > num3:
  big = num2
else :
  big = num3

print(big)
