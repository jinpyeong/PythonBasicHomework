# 1 (O)
books = ['모모', '어린왕자', '별', '돈키호테', '마당을 나온 암탉']

# 2 (O)
books.append('귀멸의 칼날')

# 3 (O)
books.insert(1, '데미안')

# 4 (O)
del books[3]

# 5 (O)
books.remove('돈키호테')

# 6 (X)
family = []
while True:
    name = input("가족 구성원의 이름 : ")
    if 'nmae' == '끝':
      break
        
    family.append(name)

print(family)

# 7 (O)
movies = ('보스베이비', '어벤져스') #가능

movies[0] = '슈퍼배드' #불가능 : 튜플은 변경이 불가능하다

movies.append('겨울왕국') #불가능 : 튜플은 변경이 불가능하다

print(movies[2]) #불가능 : 튜플의 범위를 벗어났다

del movies[0] #불가능 : 튜플은 변경이 불가능하다

print(movies[0]) #가능
