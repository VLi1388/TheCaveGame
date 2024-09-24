import time
from colorama import *
import sys
import random

from console import *
from player import *
from game import *

# def delayPrint(text):
#     for c in text:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         #time.sleep(0.1)


#to print text characters by character


# def delayPrintWord(text):
#     for word in text.split('-'):  # using '-' so that the spaces will be kept
#         sys.stdout.write(word)
#         sys.stdout.flush()
#         #time.sleep(0.3)


#to print word by word on same line

# def delayPrintRow(text):
#     for word in text.split('-'):
#         print(word)
#         #time.sleep(0.4)


# maxHP = 100
# hp = 100
# defense = 10 # represents a percentage, blocks enemy's attack
# attack = 15
# inventory = []

#main function: game()
def game():
    #player data function, this acts as the profile of the player
    # def displayPlayerProfile():
    #     #print statements
    #     print("-----------------------------------------------------------")
    #     print("-----------------------------------------------------------")
    #     #time.sleep(0.3)
    #     print(f'【{player}】\n'.center(59))
    #     #time.sleep(0.8)
    #     print(f'HP: [{hp}/{maxHP}]'.center(59))
    #     print(f'DEFENSE: [{defense}]'.center(59))
    #     print(f'ATTACK: [{attack}]'.center(59))
    #     #time.sleep(0.3)
    #     print("-----------------------------------------------------------")
    #     #time.sleep(0.3)
    #     print('【INVENTORY】\n'.center(59))
    #     #time.sleep(0.8)
    #     for item in inventory:
    #         print(f'{item}'.center(59))
    #         #time.sleep(0.3)
    #     print("-----------------------------------------------------------")
    #     print("-----------------------------------------------------------")

    #to ask if player wants to chech profile
    # def checkStatus():
    #     #time.sleep(0.3)
    #     print("-----------------------------------------------------------")
    #     #time.sleep(0.3)
    #     print(
    #         f'Check profile?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})'
    #     )
    #     #time.sleep(0.3)
    #     status = input('>>>>>')
    #     #time.sleep(0.3)
    #     if status == 'yes':
    #         displayPlayerProfile()
    #     else:
    #         print(
    #             "-----------------------------------------------------------")

    #story context
    # delayPrint(
    #     'Your eyes feel like they are glued together, after some\nstruggling, you are finally able to open them\n\n'
    # )
    # delayPrint('You find yourself laying on a rough, rocky ground\n\n')
    # delayPrint(
    #     'You feel nausea and the world seems to be swirling around\nyou\n\n')
    # delayPrint('You strenuously lift your head up\n\n')
    # delayPrint(
    #     'Your vision is blurry but you could recognize that you\nare in a cave\n\n'
    # )
    # delayPrint(
    #     'The cave is lit up by a few lanterns hanging from the wall,\nyou could see faintly a chest that is few feets away from\nyou\n\n'
    # )
    # delayPrint(
    #     'You let your head back down and continued to lay on the\nground\n\n')
    # delayPrint(
    #     'Your headache begins to fade away and your memories slowly\nreturns to you\n\n'
    # )
    
    # introStory()
    
    # # #asks for player name variable
    # # delayPrint('What was your name again?\n')
    # # #time.sleep(0.5)
    # # player = input('>>>>>')
    # # #time.sleep(0.3)
    # # print("-----------------------------------------------------------")
    
    # setName()

    # #time.sleep(0.3)

    # global hp
    # global maxHP
    # global defense
    # global attack
    #globalizing variables allow me to access variables that were stated outside of the function from inside the function

    # delayPrint(
    #         'You feel way better after taking a few minutes of rest, but\nyou could still only remember your name\n\n'
    #     )
    # delayPrint(
    #         'You stand up and decides to take a closer look at the chest\n\n')
    # delayPrint(
    #         'You slowly approach it and notices that the chest is fairly\nlarge, it seems to be made out of dark wood\n\n'
    #     )
    # delayPrint(
    #         'The chest is covered with drawings of magic spells, they\nseemed to be from the black magic branch\n\n'
    #     )

    # print(
    #         f'Open chest?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})'
    #     )
    #this is a list
    # buff_item = [
    #         'Salutem  Necklace', 'Ring of Praesidium',
    #         'Bottle of Werewolf Blood'
    #     ]
    # #salutem is health in latin; praesidium means protection in latin
    # #Salutem  Necklace boosts max health
    # #Ring of Praesidium boosts defense
    # #Bottle of Werewolf Blood boosts attack

    #time.sleep(0.3)

    #at the start of the game, the player gets a lucky draw of a random buff item
    # chest = input('>>>>>')
    # if chest == 'yes':
    #     #time.sleep(0.3)
    #     print(
    #             "-----------------------------------------------------------")
    #     #time.sleep(0.3)
    #     delayPrint(
    #             'Despite the creepy look of the chest, you reached over and\nopened it...\n'
    #         )
    #     #time.sleep(0.3)
    #     print(
    #             "-----------------------------------------------------------")
    #     #time.sleep(0.3)
    #     delayPrint(
    #             'You were lucky this time, the chest opened and only dust \nflew out of it\n\n'
    #         )
    #     #time.sleep(0.5)

    #     draw = []
    #     for i in range(0, 2):
    #         num = random.randint(1, 3)
    #         draw.append(num)

    #     if 1 in draw:
    #         print(
    #                 f'  You have obtained <{Fore.YELLOW}Salutem  Necklace{Fore.LIGHTWHITE_EX}>'
    #             )
    #         #manipulating list(adding variables to list)
    #         inventory.append(f'<{buff_item[0]}>')
    #         inventory.append('HEALTH + 20')
    #         #time.sleep(1)
    #         print(f'  MAX HP {Fore.LIGHTGREEN_EX}+20{Fore.LIGHTWHITE_EX}')
    #         #time.sleep(1)
    #         print(f'  HP {Fore.LIGHTGREEN_EX}+20{Fore.LIGHTWHITE_EX}')
    #         #operations
    #         maxHP += 20
    #         hp += 20
    #         #time.sleep(1)
    #         print(f'  Your HP is now [{hp}/{maxHP}]')
    #         #time.sleep(1)
    #         checkStatus()

    #     elif 2 in draw:
    #         print(
    #                 f'  You have obtained <{Fore.YELLOW}Ring of Praesidium{Fore.LIGHTWHITE_EX}>'
    #             )
    #         inventory.append(f'<{buff_item[1]}>')
    #         inventory.append('DEFENSE + 8')
    #         #time.sleep(1)
    #         print(f'  DEFENSE {Fore.LIGHTGREEN_EX}+8{Fore.LIGHTWHITE_EX}')
    #         defense += 8
    #         #time.sleep(1)
    #         print(f'  Your defense is now [{defense}]')
    #         #time.sleep(1)
    #         checkStatus()

    #     elif 3 in draw:
    #         print(
    #                 f'  You have obtained <{Fore.YELLOW}Bottle of Werewolf Blood{Fore.LIGHTWHITE_EX}>'
    #             )
    #         inventory.append(f'<{buff_item[2]}>')
    #         inventory.append('ATTACK + 8')
    #         #time.sleep(1)
    #         print(f'  ATTACK {Fore.LIGHTGREEN_EX}+8{Fore.LIGHTWHITE_EX}')
    #         attack += 8
    #         #time.sleep(1)
    #         print(f'  Your ATTACK is now [{attack}]')
    #         #time.sleep(1)
    #         checkStatus()

    # else:
    #   #time.sleep(0.3)
    #   print(
    #             "-----------------------------------------------------------")
    #   #time.sleep(0.3)
    #   delayPrint(
    #             'You decided to be careful\n\nBeing cautious is a good strategy, but you may have missed\nyour chance\n'
    #         )
    #   checkStatus()


    delayPrint('You pack all your stuff and begin to walk down the tunnel\n\n')
    delayPrint('The lantern flickers as you walk in the tunnel, you hear a\nlow growl from the dark\n')

    #the combat function
    def combat():
        global maxHP
        global hp
        global attack
        global defense
        enemyHP = random.randint(60, 140)
        #rounding
        enemyAtk = round(enemyHP * 0.2)

        print("-----------------------------------------------------------")
        #time.sleep(0.3)
        print(
            f'{Fore.LIGHTRED_EX}【{Fore.LIGHTYELLOW_EX}You have encountered an enemy{Fore.LIGHTRED_EX}】{Fore.LIGHTWHITE_EX}\n'
        )
        #time.sleep(0.6)
        print(
            f"Enemy information:\n  Health: [{enemyHP}]\n  Attack: [{enemyAtk}]"
        )
        #time.sleep(0.8)
        print("-----------------------------------------------------------")
        #time.sleep(0.3)

        print("Please choose your next move:")
        #time.sleep(0.5)
        delayPrintRow('  Attack-  Inventory-  Flee')

        move = input('>>>>>')

        #time.sleep(0.3)

        #this is a while loop
        while move == 'Inventory':
            displayPlayerProfile()
            print("Please choose your next move:")
            #time.sleep(0.5)
            delayPrintRow('  Attack-  Inventory-  Flee')
            move = input('>>>>>')

            #time.sleep(0.3)
            print(
                "-----------------------------------------------------------")
            #time.sleep(0.3)

        #comparison: equals to 
        while move == 'Attack' and enemyHP > attack and hp > enemyAtk:
            num = random.randint(1, 20)
            #there is a 5% chance for the enemy to dodge your attack

            #you and the enemy take turns to attack
            if num == 20:
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)
                print('The enemy dodged your attack')
                #time.sleep(0.3)
                print(f'  Enemy HP {Fore.LIGHTRED_EX}-0{Fore.LIGHTWHITE_EX}\n')
                #time.sleep(0.7)
                print(
                    f"Enemy information:\n  Health: [{enemyHP}]\n  Attack: [{enemyAtk}]"
                )
                #time.sleep(0.3)
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)
            else:
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)
                print(f'Enemy was unable to dodge your attack')
                #time.sleep(0.3)
                print(
                    f'  Enemy HP {Fore.LIGHTRED_EX}-{attack}{Fore.LIGHTWHITE_EX}\n'
                )
                #time.sleep(0.7)
                enemyHP -= attack
                print(
                    f"Enemy information:\n  Health: [{enemyHP}]\n  Attack: [{enemyAtk}]"
                )
                #time.sleep(0.3)
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)

            print('The enemy attacked\n')
            #time.sleep(0.5)
            num = num = random.randint(1, 10)
            #there is a 10% chance for the player to dodge enemy's attack
            if num == 10:
                print(f'You dodged the attack')
                #time.sleep(0.3)
                print(f'  HP {Fore.LIGHTRED_EX}-0{Fore.LIGHTWHITE_EX}\n')
                #time.sleep(0.3)
                print(f'Your HP is now [{hp}/{maxHP}]')
                #time.sleep(0.3)
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)
            else:
                print(f'You were unable to dodge the attack')
                #time.sleep(0.3)
                #operations
                print(
                    f'  HP {Fore.LIGHTRED_EX}-{enemyAtk - round(defense / 100 * enemyAtk)}{Fore.LIGHTWHITE_EX}\n'
                )
                #time.sleep(0.3)
                hp -= enemyAtk - round(defense / 100 * enemyAtk)
                print(f'Your HP is now [{hp}/{maxHP}]')
                #time.sleep(0.3)
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)

            #boolean logic: or
            #transitions into "winning page" when enemy would be defeated by your next attack
            if enemyHP < attack or enemyHP == attack:
                print("Please choose your next move:")
                #time.sleep(0.5)
                delayPrintRow('  Attack-  Inventory-  Flee')
                move = input('>>>>>')

                #time.sleep(0.3)
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)
                if move == 'Attack':
                    #time.sleep(0.3)
                    print('You made your final attack')
                    #time.sleep(0.3)
                    print(
                        f'  Enemy HP {Fore.LIGHTRED_EX}-{attack}{Fore.LIGHTWHITE_EX}\n'
                    )
                    #time.sleep(0.3)
                    print('Enemy has been defeated')
                    
                    #time.sleep(0.3)
                    print("-----------------------------------------------------------")
                    #time.sleep(0.3)

                    delayPrint('The enemy collapses before you\n\n')
                    delayPrint('It turns into a white glow and fades away\n\n')
                    delayPrint(f'{Fore.LIGHTYELLOW_EX}3{Fore.LIGHTWHITE_EX} chests dropped on the ground\n\n')

                    #loot list
                    loot_item = ['Iron Chestplate','Iron Shield','Book of Witchery','Green Crystal Shard','Book of Combat','Silver Sword']
                    bonus_loot = ['Iron Shield', 'Potion of Health', 'Silver Spear']

                    #this is a dictionary
                    loot_chest = {'chest_1': random.choice(loot_item[0:2]), 'chest_2': random.choice(loot_item[2:4]), 'chest_3': random.choice(loot_item[4:6])}
                    #this is to randomize loot drop even more
                      

                    print(f'Pick a chest to open({Fore.CYAN}1{Fore.LIGHTWHITE_EX} or {Fore.CYAN}2{Fore.LIGHTWHITE_EX} or {Fore.CYAN}3{Fore.LIGHTWHITE_EX}) ')
                    #time.sleep(0.3)
                    chest_pick = input('>>>>>')
                    #time.sleep(0.3)

                    if chest_pick == '1':
                      print("-----------------------------------------------------------")
                      #time.sleep(0.3)
                      print(f"  You have obtained <{Fore.YELLOW}{loot_chest.get('chest_1')}{Fore.LIGHTWHITE_EX}>")
                      inventory.append(f"<{loot_chest.get('chest_1')}>")
                      inventory.append('defense +6')
                      #time.sleep(1)
                      print(f'  DEFENSE {Fore.LIGHTGREEN_EX}+6{Fore.LIGHTWHITE_EX}')
                      defense += 6
                      #time.sleep(1)
                      print(f'  Your DEFENSE is now [{defense}]')
                      #time.sleep(1)
                      checkStatus()

                    if chest_pick == '2':
                      print("-----------------------------------------------------------")
                      #time.sleep(0.3)
                      print(f"  You have obtained <{Fore.YELLOW}{loot_chest.get('chest_2')}{Fore.LIGHTWHITE_EX}>")
                      inventory.append(f"<{loot_chest.get('chest_2')}>")
                      inventory.append('HP +24')
                      #time.sleep(1)
                      print(f'  HP {Fore.LIGHTGREEN_EX}+24{Fore.LIGHTWHITE_EX}')
                      hp += 24
                      #time.sleep(1)
                      print(f'  Your HP is now [{hp}/{maxHP}]')
                      #time.sleep(1)
                      checkStatus()    
                      
                    if chest_pick == '3':
                      print("-----------------------------------------------------------")
                      #time.sleep(0.3)
                      print(f"  You have obtained <{Fore.YELLOW}{loot_chest.get('chest_3')}{Fore.LIGHTWHITE_EX}>")
                      inventory.append(f"<{loot_chest.get('chest_3')}>")
                      inventory.append('attack +10')
                      #time.sleep(1)
                      print(f'  ATTACK {Fore.LIGHTGREEN_EX}+10{Fore.LIGHTWHITE_EX}')
                      attack += 10
                      #time.sleep(1)
                      print(f'  Your ATTACK is now [{attack}]')
                      #time.sleep(1)
                      checkStatus()

                    num = random.randint(1,20)
                    #there is a 5% chance to get a bonus loot drop
                    if num == 20:
                      #manipulaitng a dictionary(adding variable to dictionary)
                      loot_chest['bonus_chest'] = random.choice(bonus_loot)
                      delayPrintWord(f'{Fore.LIGHTYELLOW_EX}BONUS- LOOT- DROP{Fore.LIGHTWHITE_EX}\n')
                      #time.sleep(0.7)
                      print(f'Open chest?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})')
                      #time.sleep(0.3)
                      open_input = input('>>>>>')
                      #time.sleep(0.3)
                      if open_input == 'yes':
                        print("-----------------------------------------------------------")
                        #time.sleep(0.3)
                        print(f"  You have obtained <{Fore.YELLOW}{loot_chest.get('bonus_chest')}{Fore.LIGHTWHITE_EX}>")

                        if loot_chest.get('bonus_chest') == 'Iron Shield':
                          inventory.append(f"<{loot_chest.get('bonus_chest')}>")
                          inventory.append('defense +10')
                          #time.sleep(1)
                          print(f'  DEFENSE {Fore.LIGHTGREEN_EX}+10{Fore.LIGHTWHITE_EX}')
                          defense += 10
                          #time.sleep(1)
                          print(f'  Your DEFENSE is now [{defense}]')
                          #time.sleep(1)
                          checkStatus()

                        if loot_chest.get('bonus_chest') == 'Potion of Health':
                          inventory.append(f"<{loot_chest.get('bonus_chest')}>")
                          inventory.append('max HP +10')
                          #time.sleep(1)
                          print(f'  MAX HP {Fore.LIGHTGREEN_EX}+10{Fore.LIGHTWHITE_EX}')
                          maxHP += 10
                          #time.sleep(1)
                          print(f'  Your HP is now [{hp}/{maxHP}]')
                          #time.sleep(1)
                          checkStatus()

                        if loot_chest.get('bonus_chest') == 'Silver Spear':
                          inventory.append(f"<{loot_chest.get('bonus_chest')}>")
                          inventory.append('attack +10')
                          #time.sleep(1)
                          print(f'  ATTACK {Fore.LIGHTGREEN_EX}+10{Fore.LIGHTWHITE_EX}')
                          attack += 10
                          #time.sleep(1)
                          print(f'  Your ATTACK is now [{attack}]')
                          #time.sleep(1)
                          checkStatus()
                      else:
                        print("-----------------------------------------------------------")
                break

            #transitions into "losing page" when your health would not withstand enemy's next hit
            if hp < enemyAtk or hp == enemyAtk:
                hp = 0
                #time.sleep(0.3)
                print(
                    'The enemy made another successful strike')
                #time.sleep(0.3)
                print(f'  HP {Fore.LIGHTRED_EX}-{enemyAtk}{Fore.LIGHTWHITE_EX}\n')
                #time.sleep(0.3)
                print('You have been defeated'
                )

                #time.sleep(0.3)
                print(
                "-----------------------------------------------------------")
                #time.sleep(0.3)

                #revive method
                delayPrint('Before you could turn around to take a look, a black robe\nwas thrown on top of you\n\n')
                delayPrint('You hear a loud screech from the monster and the sound of\nit collapsing\n\n')
                delayPrint('You hear the footstep getting close to you\n\n')
                delayPrint('The robe is taken off of you\n\n')
                delayPrint('You see a person wearing a bird-like beak mask\n\n')
                delayPrint(f'{Fore.LIGHTBLUE_EX}Would you like to make a trade?\n\n')
                delayPrint(f'I will pay you {Fore.LIGHTGREEN_EX}5 HP{Fore.LIGHTBLUE_EX} for {Fore.LIGHTRED_EX}1 ATTACK{Fore.LIGHTBLUE_EX} or {Fore.LIGHTRED_EX}1 DEFENSE{Fore.LIGHTBLUE_EX}{Fore.LIGHTWHITE_EX}\n')

                #time.sleep(0.3)
                print("-----------------------------------------------------------")
                #time.sleep(0.3)

                print('Please enter the amount of DEFENSE you want to trade for')
                #time.sleep(0.3)
                #casting
                trade = int(input('>>>>>'))
                #time.sleep(0.3)
                print("-----------------------------------------------------------")
                #time.sleep(0.3)

                while trade > defense:
                  print('Invalid input')
                  #time.sleep(0.3)
                  print('Please enter the amount of DEFENSE you want to trade for')
                  #time.sleep(0.3)
                  trade = int(input('>>>>>'))
                  #time.sleep(0.3)
                  print("-----------------------------------------------------------")
                  #time.sleep(0.3)

                print('You made your choice')
                hp += trade * 5
                defense -= trade
                #time.sleep(0.3)
                print(f'  HP {Fore.LIGHTGREEN_EX}+{trade * 5}{Fore.LIGHTWHITE_EX}')
                #time.sleep(0.3)
                print(f'  DEFENSE {Fore.LIGHTRED_EX}-{trade}{Fore.LIGHTWHITE_EX}')
                #time.sleep(0.3)
                print(f'Your HP is now [{hp}/{maxHP}]')
                #time.sleep(0.3)
                print(f'Your DEFENSE is now {defense}')

                #time.sleep(0.3)
                print("-----------------------------------------------------------")
                #time.sleep(0.3)

                print('Please enter the amount of ATTACK you want to trade for')
                #time.sleep(0.3)
                trade = int(input('>>>>>'))
                #time.sleep(0.3)
                print("-----------------------------------------------------------")
                #time.sleep(0.3)

                while trade > attack:
                  print('Invalid input')
                  #time.sleep(0.3)
                  print('Please enter the amount of ATTACK you want to trade for')
                  #time.sleep(0.3)
                  trade = int(input('>>>>>'))
                  #time.sleep(0.3)
                  print("-----------------------------------------------------------")
                  #time.sleep(0.3)
                  
                print('You made your choice')
                hp += trade * 5
                attack -= trade
                #time.sleep(0.3)
                print(f'  HP {Fore.LIGHTGREEN_EX}+{trade * 5}{Fore.LIGHTWHITE_EX}')
                #time.sleep(0.3)
                print(f'  ATTACK {Fore.LIGHTRED_EX}-{trade}{Fore.LIGHTWHITE_EX}')
                #time.sleep(0.3)
                print(f'Your HP is now [{hp}/{maxHP}]')
                #time.sleep(0.3)
                print(f'Your ATTACK is now {attack}')

                break

            print("Please choose your next move:")
            #time.sleep(0.5)
            delayPrintRow('  Attack-  Inventory-  Flee')
            move = input('>>>>>')

            #time.sleep(0.3)
            print(
                "-----------------------------------------------------------")
            #time.sleep(0.3)

            while move == 'Inventory':
                displayPlayerProfile()
                print("Please choose your next move:")
                #time.sleep(0.5)
                delayPrintRow('  Attack-  Inventory-  Flee')
                move = input('>>>>>')

                #time.sleep(0.3)
                print(
                    "-----------------------------------------------------------"
                )
                #time.sleep(0.3)
                
        if move == 'Flee':
            print(
                "-----------------------------------------------------------")
            #time.sleep(0.3)
            print(
                'You took action before the enemy noticed and was able to\nescape\n'
            )
            #time.sleep(1)
            print('But suddenly, you hear the monster screech and a then loud\nthud hitting the ground\n')
            #time.sleep(1)
            print("You immediately looked back but didn't see anyone")
            #time.sleep(0.3)
            print(
                "-----------------------------------------------------------")
            #time.sleep(0.3)

    combat()

    delayPrint('You looked back at the monter’s corpse\n\n')
    delayPrint(f'{Fore.LIGHTYELLOW_EX}...Disgusting{Fore.LIGHTWHITE_EX}\n\n')
    delayPrint('You continue to walk down the tunnel\n')
    #time.sleep(0.3)
    print("-----------------------------------------------------------")
    #time.sleep(0.3)
    print(f'{Fore.LIGHTRED_EX}!!!ROAR!!!{Fore.LIGHTWHITE_EX}\n')
    delayPrint('Another monster jumped out from the corner on the hallway\n\n')
    delayPrint(f'{Fore.LIGHTYELLOW_EX}...He probably came to revenge his friend{Fore.LIGHTWHITE_EX}\n')

    #fight one more enemy
    combat()

    delayPrint('Another monster corpse lay quietly on the ground\n\n')
    delayPrint('Disgusted by its looks, you turned around and continued to\nwalk down the tunnel\n\n')
    delayPrint('The journey was calm and the only noise was of the fire\nburning in your lantern\n\n')
    delayPrint('You walked for who knows how long, after turns and corners,\nyou finally saw light coming from the end of the tunnel\n\n')
    delayPrint(f'{Fore.LIGHTYELLOW_EX}...That must be the exit{Fore.LIGHTWHITE_EX}\n')

    #time.sleep(0.3)
    print("-----------------------------------------------------------")
    #time.sleep(0.3)

    delayPrint('You rushed through the gate of light and is welcomed by an\nopen world filled with fresh air and green plants\n\n')
    delayPrint(f'{Fore.LIGHTYELLOW_EX}...I’m finally out{Fore.LIGHTWHITE_EX}\n\n')
    delayPrint('You lay down on the grass and enjoys the spring breeze\n\n')
    delayPrint('Although you have escaped from the cave, your mysteries are\nstill unsolved\n\n')
    delayPrint('You do not know why you would be abandoned in a cave\n\n')
    delayPrint('You do not know where you are\n\n')
    delayPrint('You do not know what the purpose behind your journey is\n\n')
    delayPrint('But you decide to ignore them for now and take a nap\n\n')
    delayPrint('......\n\n')
    delayPrint('You feel refreshed and revived after taking a nap on the\nsoft grass field\n\n')
    delayPrint('You know that it is the time to continue with your journey\nnow\n\n')
    delayPrint('You stand up and and goes off into the distance\n')
    
    #time.sleep(0.3)
    print("-----------------------------------------------------------")
    #time.sleep(0.3)

#to print text in center of console, console on school computer is 59 long
greet = 'Welcome to The Cave'.center(59)
#upper case
delayPrint(Fore.LIGHTRED_EX + greet.upper())
print('')

#time.sleep(0.3)

print(Fore.LIGHTWHITE_EX +
      "-----------------------------------------------------------")

#time.sleep(0.7)

delayPrintWord(
    'This- is- a- rougelike- game,- which- means- that- your- every- \nexperience- with- the- game- would- be- different\n'
)

#time.sleep(0.5)

print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

#time.sleep(1.8)

print(
    f'Watch Tutorial?({Fore.CYAN}Press Enter{Fore.LIGHTWHITE_EX} to watch or {Fore.CYAN}Print "no"{Fore.LIGHTWHITE_EX} to skip)'
)
#time.sleep(0.3)
tutorial_watch = input('>>>>>')

#time.sleep(0.5)

print("-----------------------------------------------------------")


def tutorial():
    #time.sleep(0.5)
    print('For example:')

    #time.sleep(0.5)

    print("\nPlease choose your next move:")
    #time.sleep(0.5)
    delayPrintRow('  Attack-  Inventory-  Flee')

    print('>>>>>', end='')  # so that fucntion would print on same line
    #time.sleep(0.3)
    delayPrint('Attack\n')

    #time.sleep(0.7)

    #concatenate
    print(Fore.LIGHTBLUE_EX +
          '  Your character attacked and dealt 15 damage!' +
          Fore.LIGHTWHITE_EX)
    #time.sleep(0.3)
    print("-----------------------------------------------------------")
    #time.sleep(0.7)


if tutorial_watch == 'no':
    #time.sleep(0.3)
    print(Fore.LIGHTYELLOW_EX + 'GAME LOADING', end='')
    delayPrint('......\n' + Fore.LIGHTWHITE_EX)
    #time.sleep(0.3)
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    #time.sleep(1.5)
    game()
else:
    print("-----------------------------------------------------------")
    #time.sleep(0.7)
    instructions = 'The game is played by ' + Fore.LIGHTGREEN_EX + 'entering text' + Fore.LIGHTWHITE_EX + ' as your choice of\nmovement\n\n'
    delayPrint(instructions)
    #time.sleep(0.7)
    tutorial()
    while True:
        print(
            f'Would you like to watch the tutorial again?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})'
        )
        #time.sleep(0.3)
        replay_t = input('>>>>>')
        #time.sleep(0.3)
        print("-----------------------------------------------------------")
        #this is an if-else loop
        if replay_t == 'yes':
            tutorial()
        else:
            print(Fore.LIGHTYELLOW_EX + 'GAME LOADING', end='')
            delayPrint('......\n' + Fore.LIGHTWHITE_EX)
            #time.sleep(0.3)
            print(
                "-----------------------------------------------------------")
            print(
                "-----------------------------------------------------------")
            #time.sleep(1.5)
            #calling the game() function to run the whole game
            game()
            break

#this is a while loop
while True:
  print(f'Would you like to play again?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})')
  #time.sleep(0.3)
  game_replay = input('>>>>>')
  #time.sleep(0.3)
  print("-----------------------------------------------------------")
  if game_replay == 'yes':
    print(Fore.LIGHTYELLOW_EX + 'GAME LOADING', end='')
    delayPrint('......\n' + Fore.LIGHTWHITE_EX)
    #time.sleep(0.3)
    print(
                "-----------------------------------------------------------")
    print(
                "-----------------------------------------------------------")
    #time.sleep(1.5)
    game()
  else:
    end = 'thanks for playing'.center(59)
    delayPrint(Fore.LIGHTYELLOW_EX + end.upper())
    print('')
    #to break out of loop and stop program(end game)
    break