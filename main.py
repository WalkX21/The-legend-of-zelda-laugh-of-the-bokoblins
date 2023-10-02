from random import *
from time import *
from hero import Hero

knight = Hero('Richard', 50, 25, 20, 'sword')
dragon = Hero('Dragon', 100, 25, 10, 'flame')

print('Middle-Earth is in danger! A valiant knight is hurrying to the rescue...')
knight.print_info()


sleep(5)
print(knight.name + ' is going through the woods. Suddenly, he sees a petty robber on his way...')


sleep(5)
rascal = Hero('Peter', 20, 5, 5, 'knife')
rascal.print_info()

sleep(5)

if input('Fight? (yes/no) >>') == 'yes':
   print('\nLET THE FIGHT BEGIN!\n')
   sleep(5)
   knight.fight(rascal)
   sleep(5)


   if knight.health > 0:
       knight.health = 100
       knight.power *= 2
       knight.armor = 10*2
       print('\n' + knight.name + ' regained his power and became more experienced. Now, the power of his strike is: ' + str(knight.power) + ', and the armor class:' + str(knight.armor) + '\n')


sleep(5)
print('\nFinally ' + knight.name + ' gets to the dungeon!')
dragon.print_info()


print('\nLET THE FIGHT BEGIN!\n')
sleep(5)
knight.fight(dragon)


    




    