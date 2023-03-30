# 1 (O)
# pokemonModule.py
import random

class Pokemon:
  def __init__(self, name):
    self.name = name
        
  def __str__(self):
    return '이름은 {}, HP는 700'.format(self.name)

class Pikachu(Pokemon):
  def __init__(self, name, skill):
    super().__init__(name)
    self.skill = skill

  def set_name(self):
    self.name = str(input("피카츄의 이름은? : "))
  
  def pikachu_skill(self):
    print("{}의 백만볼트!".format(self.name))

    effect = random.randint(1,6)
        
    if effect == 1:
      print("효과가 굉장했다!")
    elif 2 <= effect <= 3:
      print("효과가 평범했다.")
    elif 4 <= effect <= 6:
      print("효과가 별로인듯하다....")
        
    return self.skill


class Eevee(Pokemon):
  def __init__(self, name, skill):
    super().__init__(name)
    self.skill = skill

  def set_name(self):
    self.name = str(input("이브이의 이름은? : "))
  
  def eevee_skill(self):
    print("{}의 몸통박치기!".format(self.name))

    effect = random.randint(1,6)
        
    if effect == 1:
      print("효과가 굉장했다!")
    elif 2 <= effect <= 3:
      print("효과가 평범했다.")
    elif 4 <= effect <= 6:
      print("효과가 별로인듯하다....")
        
    return self.skill

# main.py
import pokemonModule

pikachu1 = pokemonModule.Pikachu('name', 'skill')
pikachu1.set_name()
pikachu1.pikachu_skill()

eevee1 = pokemonModule.Eevee('name', 'skill')
eevee1.set_name()
eevee1.eevee_skill()

# 2 (O)
# 새파일.txt
1 번째 줄입니다.
2 번째 줄입니다.
3 번째 줄입니다.
4 번째 줄입니다.
5 번째 줄입니다.
6 번째 줄입니다.
7 번째 줄입니다.
8 번째 줄입니다.
9 번째 줄입니다.
10 번째 줄입니다.

# 3 (O)
# 새파일.txt
안녕하세요.

# 새파일.tx

# 새파일.tx
안녕하세요.
