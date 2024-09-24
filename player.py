import time
from colorama import *
import sys

from console import *

maxHP = 100
hp = 100
defense = 10 # represents a percentage, blocks enemy's attack
attack = 15
inventory = []
name = "" #***

# asks for player to input name
def setName(inputName):
    name = inputName #***
    
# adds an item to the player inventory
def addInventory(item):
    inventory.append(item)
    
def getMaxHP():
    return maxHP

def addMaxHP(num):
    maxHP += num
    
def getHP():
    return hp

def addHP(num):
    hp += num
    
def getDefense():
    return defense
    
def addDefense(num):
    defense += num
    
def getAttack():
    return attack

def addAttack(num):
    attack += num

# displays player profile
def displayPlayerProfile():
        printSeparation()
        # time.sleep(0.3)
        print(f'【{player}】\n'.center(59))
        #time.sleep(0.8)
        print(f'HP: [{hp}/{maxHP}]'.center(59))
        print(f'DEFENSE: [{defense}]'.center(59))
        print(f'ATTACK: [{attack}]'.center(59))
        #time.sleep(0.3)
        printSubSep()
        #time.sleep(0.3)
        print('【INVENTORY】\n'.center(59))
        #time.sleep(0.8)
        for item in inventory:
            print(f'{item}'.center(59))
            #time.sleep(0.3)
        printSeparation()

# asks if the player wants to check their profile
def checkStatus():
        #time.sleep(0.3)
        printSubSep()
        #time.sleep(0.3)
        print(
            f'Check profile?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})'
        )
        #time.sleep(0.3)
        status = input('>>>>>')
        #time.sleep(0.3)
        if status == 'yes':
            displayPlayerProfile()
        else:
            printSubSep()
            