# 1

print("\'python\'은 프로그래밍 언어입니다.")

# 2

temperature1 = 32

temperature2 = 32

convert1 = (temperature1 - 32) / 18
convert2 = (temperature2 * 1.8) + 32

print('화씨 {}도는 섭씨 {}도'.format(temperature1, convert1))
print('섭씨 {}도는 화씨 {}도'.format(temperature2, convert2))

# 3

year = 2023

# 4

3번째줄 , 4번째줄

# 5

n

자
0과 문자 '10'은 다르다.

# 6

s = '공격받은 몬스터는 {}의 데미지를 받았습니다.'
print(s.format(10)
print(s.format(50)
print(s.format(297)

# 7

age = int(input('\'당신의 나이는?\''))
year = 2023 - age
print('당신의 올해 나이는 {}살 입니다. 당신은 {}년에 태어났습니다.'.format(age, year))

# 8

def smile(s):
    end = ' :D'
    print(s + end)

smile('안녕하세요')

# 9
      
def exchange(won):
    dollar = won / 1300
    return dollar
      
print(exchange(2000))
print(exchange(13000))
print(exchange(1000000))

won = int(input('환전할 원화 : '))
dollar = exchange(won)
print('당신은 ${} 를 환전했습니다.'.format(dollar))
      
# 10
      
a = True
b = False
      
# 11
      
False
True
False
True
False
True
True
True
False
True
False
False
False

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
