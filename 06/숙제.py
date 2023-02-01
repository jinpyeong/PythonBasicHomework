# 1

1 2 3 4 5 6 7 8 9
3 6 9 12 15
5 6 7 8 9 10
0 1 2 3 4
10 8 6 4 2

# 2

number = int(input('숫자를 입력하세요.'))

for i in range(number):
    print('I love Python')
    
# 3

for x in range(2002, 2051, 4):
    print(x)
    
# 4

while True:
    score = int(input('점수 : '))
    
    if score == -1:
        break
    
    if score >= 60 :
        print('합격')
    else :
        print('불합격')
        
# 5

for i in range(11):    
    if i == 7:
        continue
    print("The Number is :" , i)
    
# 6

n = int(input('숮자를 입력해주세요.'))

for i in range(2, n+1):
    is_prime = True
    
    # 코드 작성
    for i in range(@@@, @@@, @@@):
        if @@@@ == 0:
            is_prime = False
    
    if is_prime:
        print(i, end=' ')
