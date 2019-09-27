
# coding: utf-8

# In[ ]:


import random
import keyboard

class Play():
    def low_damage():
        damage = random.randint(18,26)
        return damage
    
    def heavy_damage():
        damage = random.randint(10,36)
        return damage
    
    def heal():
        heal=random.randint(18,26)
        return heal


# In[ ]:


class Player(Play):
    health=100
    name = 'Player 1'

class Computer(Play):
    health=100
    name = 'Player 2'


# In[ ]:


# Вывод уровеня здоровья каждого игрока
def health_state():
    print('{} health: {}'.format(player_1.name, player_1.health))
    print('{} health: {}'.format(player_2.name, player_2.health))


# In[ ]:


# Функция проверяет завершилась ли игра, если уровень здоровья одного из игроков упал ниже нуля.
def game_over():
    if curr_player.health <= 0: 
        print('{} win. Game over'.format(next_player.name))
        return False 
    elif next_player.health <= 0:
        print('{} win. Game over'.format(curr_player.name))
        return False 
    else:
        return True


# In[ ]:


# Действие вибирается случаныйным образом из 3-х возможных, для каждого присваивается свой номер.
# Если уровень здоровья компьютера ниже 35, выполняется выбор из 2-х вариантов.
    
def action():
    if player_2.health < 35:
        action = random.choice([1,3])
    else:
        action = random.choice([1,2,3])
        
    # Для каждого действия вызывается соответствующая функция из класса Play        
    if action == 1:
        damage_level = next_player.low_damage()
        next_player.health -= damage_level
        print('{} used low damage -{}'.format(curr_player.name,damage_level))
        
    elif action == 2:
        damage_level = next_player.heavy_damage()
        next_player.health-= damage_level
        print('{} used heavy damage -{}'.format(curr_player.name,damage_level))
        
    else:
        heal_level = curr_player.heal()
        curr_player.health+=heal_level
        print('{} healed himself +{}'.format(curr_player.name,heal_level))
        
    health_state()


# In[ ]:


player_1 = Player
player_2 = Computer


# In[ ]:


# Выбор первого игрока происходит рандомно, 1 - для игрока, 2 - для компьютера.
# Curr_player хранит текущего игрока, а next_player - чей ход будет следующим.

curr_player = random.choice([1,2])
if curr_player == 1:
    curr_player = player_1
    next_player = player_2
    print ('>> You are {}! To start press space'.format(player_1.name))
    # Все дейтсвия игрока происходят по клавише space.
    keyboard.wait('space')
else: 
    curr_player = player_2
    next_player = player_1
    print('>> {} started'.format(player_2.name))

# Тело игры. Игра продолжается, пока функция game_over не вернет False.    
game = game_over()
while game:
    action()
    # Текущий игрок становится следующим, а следующий текущим.
    if curr_player == player_1:
        curr_player = player_2
        next_player = player_1
    else:
        curr_player = player_1
        next_player = player_2
        print('--------------------------------------------------------')
        print('>> Your turn. Press space to attack enemy or heal yourself')
        keyboard.wait('space')
    print('--------------------------------------------------------')
    game = game_over()

