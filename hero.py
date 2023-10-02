from random import *
from time import *

class Hero():
    # class constructor
    def __init__(self,name,health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor 
        self.power = power
        self.weapon = weapon

    # print character info: (propriétés)
    def print_info(self):
        print('->',self.name)
        print('Health level: ',self.health)
        print('Armor class: ', self.armor)
        print('Power of the strike: ', self.power)
        print('Weapon: ', self.weapon, '\n')

    #striking another character

    def strike(self,enemy):

        attack = randint(self.power-5, self.power+5)
        print('-> STRIKE! ' + self.name + ' attacks ' + enemy.name + ' with power ' + str(attack) + ', using ' + self.weapon + '\n')

        enemy.armor -= attack # enemy.armor = enemy.armor - attatck
        if enemy.armor < 0:
            enemy.health += enemy.armor # enemy.health = enemy.health + enemy.armor
            enemy.armor = 0

        print(enemy.name + ' swayed.\nArmor class dropped to ' + str(enemy.armor) + ', and health level dropped to ' + str(enemy.health) + '\n')


    #starting a fight

    def fight(self, enemy):

        while self.health and enemy.health > 0:
           self.strike(enemy)
           if enemy.health <= 0:
               print(enemy.name, 'has fallen in this difficult battle!\n')
               break
           sleep(5)
 
           enemy.strike(self)
           if self.health <= 0:
               print(self.name, 'has fallen in this difficult battle!\n')
               break
           sleep(5)