# 12

1
4
5

# 13

def even_odd(number) :
    if number % 2 == 0:
        print("짝수")
    else:
        print("홀수")


number = int(input("숫자 입력 : "))
even_odd(number)

# 14

num1 = int(input("input number1: "))
num2 = int(input("input number2: "))
num3 = int(input("input number3: "))

if num1 < num2 and num1 < num3:
    print('{}이 가장 작은 숫자입니다.'.format(num1))
elif num2 < num1 and num2 < num3:
    print('{}이 가장 작은 숫자입니다.'.format(num2))
elif num3 < num1 and num3 < num2:
    print('{}이 가장 작은 숫자입니다.'.format(num3))
else:
    print("입력하신 숫자 중 같은 숫자가 있습니다.")

# 15

def expense(transportation):
    adult_expense = 0
    child_expense = 0
    
    if transportation == 'Bus':
      adult_expense = 40000
    elif transportation == 'Ship':
      adult_expense = 30000
    elif transportation == 'Airplane':
      adult_expense = 70000
        
    child_expense = adult_expense / 2
  
    print('{}의 성인 요금은 {}원, 어린이 요금은 {}원 입니다.'.format(transportation, adult_expense, child_expense))


transportation = input("사용할 교통편 : ")
expense(transportation)

# 16

for i in range(7, 101, 7):
  print(i)
  
i = 0
while i <= 100:
    i = i + 1
    if i % 7 == 0:
        print(i)
        
# 17

while True:
    capital = input('한국의 수도는? : ')
    
    if capital == '그만' : 
      break
    elif capital == '서울':
      print("정답입니다.")
    else :
      print("오답입니다.")
      
# 18

while True:
    score = int(input("점수: "))
    
    if 81 <= score <= 100:
      print("A등급")
    elif 61 <= score <= 80:
      print("B등급")
    elif 41 <= score <= 60:
      print("C등급")
    elif 21 <= score <= 40:
      print("D등급")
    elif 0 <= score <= 20:
      print("E등급")
    else:
      print("잘못된 점수입니다.")
      break
