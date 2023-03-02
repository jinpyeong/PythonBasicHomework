# 1 (O)
scores = [0] * 5

for i in range(5):
    scores[i] = int(input('{}번 학생의 성적 입력: '.format(i+1)))

print('--- 입력된 값 ---')

for i in range(5):
    print('{}번 학생의 성적: {}'.format(i+1, scores [i]))
    
# 2 (O)
scores = [0] * 5

for i in range(5):
    scores[i] = int(input('{}번 학생의 성적을 입력하세요: '.format(i+1)))

for i in range(5):
    if scores[i] >= 60:
        print('{}번 학생 합격'.format(i+1))
    else:
        print('{}번 학생 불합격'.format(i+1))
        
# 3 (O)
total = 0

scores = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
for score in scores:
    if score >= 50:
        print(score)
    else:
        continue

    total = total + score
print(total)

# 4 (O)
price_list = [1000, 2300, 9900, 15000]
for price in price_list:
    sale_price = (price / 10) + price
    print("{}원의 결제 금액은 {}원 입니다.".format(price, sale_price))
    
# 5 (X)
