import sys

from player import *
from console import *

def game():
    introStory()
    
    delayPrint('What was your name again?\n')
    inputName = input('>>>>>') #***
    setName(inputName)
    printSubSep()
    
    approachChest()
    chest = input('>>>>>')
    chestAction(chest)
    
    delayPrint('You pack all your stuff and begin to walk down the tunnel\n\n')
    delayPrint('The lantern flickers as you walk in the tunnel, you hear a\nlow growl from the dark\n')
    
def introStory():
    delayPrint(
        'Your eyes feel like they are glued together, after some\nstruggling, you are finally able to open them\n\n'
    )
    delayPrint('You find yourself laying on a rough, rocky ground\n\n')
    delayPrint(
        'You feel nausea and the world seems to be swirling around\nyou\n\n')
    delayPrint('You strenuously lift your head up\n\n')
    delayPrint(
        'Your vision is blurry but you could recognize that you\nare in a cave\n\n'
    )
    delayPrint(
        'The cave is lit up by a few lanterns hanging from the wall,\nyou could see faintly a chest that is few feets away from\nyou\n\n'
    )
    delayPrint(
        'You let your head back down and continued to lay on the\nground\n\n')
    delayPrint(
        'Your headache begins to fade away and your memories slowly\nreturns to you\n\n'
    )
    
def approachChest():
    delayPrint(
            'You feel way better after taking a few minutes of rest, but\nyou could still only remember your name\n\n'
        )
    delayPrint(
            'You stand up and decides to take a closer look at the chest\n\n')
    delayPrint(
            'You slowly approach it and notices that the chest is fairly\nlarge, it seems to be made out of dark wood\n\n'
        )
    delayPrint(
            'The chest is covered with drawings of magic spells, they\nseemed to be from the black magic branch\n\n'
        )
    print(
            f'Open chest?({Fore.CYAN}yes{Fore.LIGHTWHITE_EX} or {Fore.CYAN}no{Fore.LIGHTWHITE_EX})'
        )