import random
from colorama import *

from player import *

buff_item = ['Salutem  Necklace', 'Ring of Praesidium', 'Bottle of Werewolf Blood']
    #salutem is health in latin; praesidium means protection in latin
    #Salutem  Necklace boosts max health
    #Ring of Praesidium boosts defense
    #Bottle of Werewolf Blood boosts attack
    
def chestAction(chest):
    if chest == 'yes':
        printSubSep()
        delayPrint('Despite the creepy look of the chest, you reached over and\nopened it...\n')
        printSubSep()
        delayPrint('You were lucky this time, the chest opened and only dust \nflew out of it\n\n')

        num = random.randint(1, 3)
        
        match num:
            case 1:
                print(f'  You have obtained <{Fore.YELLOW}Salutem  Necklace{Fore.LIGHTWHITE_EX}>')
                addInventory(f'<{buff_item[0]}>' + "HEALTH + 20")
                addMaxHP(20)
                print(f'  MAX HP {Fore.LIGHTGREEN_EX}+20{Fore.LIGHTWHITE_EX}')
                addHP(20)
                print(f'  HP {Fore.LIGHTGREEN_EX}+20{Fore.LIGHTWHITE_EX}')
                print(f'  Your HP is now [{hp}/{maxHP}]')
                checkStatus()
            case 2:
                print(f'  You have obtained <{Fore.YELLOW}Ring of Praesidium{Fore.LIGHTWHITE_EX}>')
                addInventory(f'<{buff_item[1]}>' + "DEFENSE + 8")
                addDefense(8)
                print(f'  DEFENSE {Fore.LIGHTGREEN_EX}+8{Fore.LIGHTWHITE_EX}')
                print(f'  Your DEFENSE is now [{defense}]')
                checkStatus()
            case 3:
                print(f'  You have obtained <{Fore.YELLOW}Bottle of Werewolf Blood{Fore.LIGHTWHITE_EX}>')
                addInventory(f'<{buff_item[2]}>' + "ATTACK + 8")
                addAttack(8)
                print(f'  ATTACK {Fore.LIGHTGREEN_EX}+8{Fore.LIGHTWHITE_EX}')
                print(f'  Your ATTACK is now [{attack}]')
                checkStatus()
    else:
      printSubSep()
      delayPrint('You decided to be careful\n\nBeing cautious is a good strategy, but you may have missed\nyour chance\n')
      checkStatus()