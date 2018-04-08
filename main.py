import random
class POINT(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y 

class REWARD(POINT):
  def __init__(self, x, y,name):
    super(REWARD, self).__init__(x,y)
    self.name = name
class ROBO(POINT):
  def move_up(self):
    if self.y < 10:
     self.y = y + 1
    else:
     print('Movimento proibido')
  def move_down(self):
    if self.y > 0:
     self.y = y - 1  
    else:
     print('Movimento proibido')
  def move_left(self):
    if self.x > 0:
     self.x = x - 1  
    else:
     print('Movimento proibido')
  def move_right(self):
    if self.x < 10:
     self.x = x + 1
    else:
     print('Movimento proibido')    
def check_reward(ROBO,REWARD):
  ok = False
  for REWARD in REWARDS:
    if REWARD.x == ROBO.x and REWARD.y == ROBO.y:
      ok = True
      print("O Robô achou a recompensa %s",REWARD.name)
  return ok


r1 = REWARD(random.randint(0, 10), random.randint(0, 10), 'moeda de ouro')
r2 = REWARD(random.randint(0, 10), random.randint(0, 10), 'moeda de prata')
r3 = REWARD(random.randint(0, 10), random.randint(0, 10), 'Poção de vida')
r4 = REWARD(random.randint(0, 10), random.randint(0, 10), 'Espada do amanhecer')
r5 = REWARD(random.randint(0, 10), random.randint(0, 10), 'diamante')


rewards = [r1, r2, r3, r4, r5]
robot = ROBO(random.randint(0, 10), random.randint(0, 10))
for i in range(10):
  movimento = raw_input("Digite up, down, left ou right para o movimento: ")
  if movimento == 'up':
     robot.move_up()
  elif movimento == 'down':   
     robot.move_down()
  elif movimento == 'left':   
     robot.move_left()
  elif movimento == 'right':   
     robot.move_right()
  else:
    print('Movimento inválido')
    continue
print(robot)
check_reward(robot, rewards)   
     
     
     
     