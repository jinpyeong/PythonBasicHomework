# 1
x = int(input('나이를 입력하세요.'))

if 10 <= x < 20:
  print('10대')
elif 20 <= x < 30:
  print('20대')
elif 30 <= x < 40:
  print('30대')
else :
  print('10대 미만 40대 이상입니다.')
  
  
# 2
B


# 3
while True:

  
  
# 4
count = int(input('반복할 횟수를 입력하세요.'))

i = 0
while i < count:
    print('Hello, world!' , i)
    i = i + 1
    
    
# 5
i = 0
result = 0
 
while i < 100:
    i = i + 1
    if i % 2 == 1:
      print(i)
      result = result + i

print(result)


# 6
print('-' * 40)
print('cm\tmm\tm\tinch')
print('-' * 40)

cm = 10

while cm < 100:
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.3937
  
    print(f'{cm}\t{mm}\t{m}\t{inch}')
            
    cm += 10
    
print('-' * 40)
