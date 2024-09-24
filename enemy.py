

enemyHP = 0
enemyAtk = 0

def resetEnemy():
    enemyHP = random.randint(60, 140)
    enemyAtk = round(enemyHP * 0.2)
    
    