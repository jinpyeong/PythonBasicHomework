# 1
a = 0.1 : 숫자형
b = '''Python 많이 배웠다'''  : 문자열
c = ['철수', ':', '영희'] : 리스트
d = '나이 : 12' : 문자열
e = ('banana', 'grape', 'apple', 'melon') : 튜플
f = "100" : 문자열
g = 100.2 : 숫자형
h = {'김밥':3000, '떡볶이':5000, '콜라':2000} : 딕셔너리
i = -100 : 숫자형
j = {'key': 'value'} : 딕셔너리
k = (2021, 2022, 2023) : 튜플
l = {'1', '2', '3'} : 집합
m = '2023' + '03' : 문자열
n = 2023 + 03 : 숫자형

# 2
철수는 13살 입니다.
영희는 12살 입니다.

# 3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
    
  def get_age(self):
    return self.age
    
  def __str__(self):
      return '{}, {}'.format(self.name, self.age)
    
a = Person('철수', 13);
b = Person('영희', 12);
 
print(a)
print(b)

# 4
import random

class Eevee:
    def __init__(self, name, skill):
      self.name = name
      self.skill = skill

    def get_name(self):
        self.name = str(input("포켓몬의 이름은? : "))
        return self.name
  
    def get_skill(self):
        print("{}의 몸통박치기!".format(self.name))

        effect = random(1,6)
        
        if effect == 1:
            print("효과가 굉장했다!")
        elif 2 <= effect <= 3:
            print("효과가 평범했다.")
        elif 4 <= effect <= 6:
            print("효과가 별로인듯하다....")
        
        return self.skill

    def __str__(self):
        return '이름은 {}, HP는 700'.format(self.name)
    
eevee1 = Eevee('name', 'skill')

print(eevee1)
