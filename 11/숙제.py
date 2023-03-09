# 1
dic1 = {'key': 'value'} (O)
dic2 = {1: ['안녕하세요'] (X)
dic3 = ['철수', ':', '영희'] (O)
dic4 = {'1', '2', '3'} (X)
dic5 = ('사과', ':', 'apple') (X)
dic6 = '나이 : 12' (X)
dic7 = 100.2 (X)
dic8 = {'김밥':3000, '떡볶이':5000, '콜라':2000} (O)

# 2
A = set([6, 2023, 2, 1, 3, 5, 10, 100, 283])
B = set([3, 4, 6, 22, 100, 302, 2022])

print(A & B) : {3, 6, 100}

print(A | B) : {1, 2, 3, 4, 5, 6, 10, 22, 100, 283, 302, 2023, 2022}

print(A - B) : {1, 2, 5, 10, 283, 2023}

print(B - A) : {4, 22, 302, 2022}
        
# 3
def print_command():
    print('''1. 아이스크림 추가
2. 아이스크림 가격 수정
3. 아이스크림 삭제
4. 아이스크림 출력
5. 종료''')

def print_product(product):
    print('*'*50)
    for key in product.keys():
        print('{} : {}'.format(key, product[key]))
    print('*'*50)

product = {'메로나': 1000,
       '비비빅': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

while True:
    print_command()
    command = input('작업을 선택하세요. ')
    if command == '1':
        ice_cream = input('추가할 아이스크림 : ')
        price = input('가격 : ')
        product[ice_cream] = price
    elif command == '2':
        ice_cream = input('수정할 아이스크림 : ')
        price = int(input('가격 : '))
        product[ice_cream] = price
    elif command == '3':
        ice_cream = input('삭제할 아이스크림 : ')
        del product[ice_cream]
    elif command == '4':
        print_product(product)
    elif command == '5':
        break
