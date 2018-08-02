import random
computer = random.randint(1,3)
player =int(input('请出拳'))
if ((player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer ==1)):
    print('电脑输了')
elif player == computer:
    print('平手')
else:
    print('玩家输了') 
