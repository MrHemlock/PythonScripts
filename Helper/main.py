# This program is a mockup of a combat system for a text game I may make. It is a project
# I chose to do because of the variety of skills it would teach me, seeing as this is
# my first ever Python program. It is standalone now, but may be integrated into a larger
# program in the future.
# The program is not yet finished. There is a bug where, on runs other than the first,
# the game will crash due to a dictionary value in stats.py stats.playerStats[health]
# being noneType. I'll try to fix that. It was found on 12/21/17.

import os # For cls command, to clear screen
import time # For wait command, to add a time delay
import random # For randomly generating numbers
import stats # To get stats for various actions

# The bonuses and debuffs for choosing different stances. They will be randomly chosen from the list.
attackBonus = [2, 3, 4]
attackDebuff = [2, 3, 4]
defendBonus = [2, 3, 4]
defendDebuff = [2, 3, 4]

# Checks if on Windows, and uses cls if so. Otherwise, tries clear, which works on Mac and Linux. Otherwise passes.
try:
    if os.name() == 'nt':
        os.system('cls')
    else:
        os.system('clear')
except TypeError:
    pass

# To check if the player or enemy successfully evaded the attack. If a random integer between 1 and 100 is in a range from 1 to the character's max evade percentage (value*2 + 6) then the evade is returned True.
def evade_check(evade):
    return bool(random.randint(1, 100) in list(range(1, evade*2 + 6))) 

# Gets the damage from generating a number between the character's minimum and maximum attack stat, then applies buffs or debuffs.
def damage_calculator(stance, isPlayer, minAttack, maxAttack):
    if isPlayer:
        damageDealt = random.randint(stats.playerStats['minAttack'], stats.playerStats['maxAttack']) 
        # Randomly generates damage dealt using the character's stats
    else:
        damageDealt = random.randint(minAttack, maxAttack)
    if stance == 'attack':
        damageDealt =  damageDealt + random.choice(attackBonus) # Gives a bonus for choosing the Attack stance
        return damageDealt
    elif stance == 'defend':
        damageDealt = damageDealt - random.choice(defendDebuff)
        if damageDealt <= 0:
            damageDealt = 1
        return damageDealt
    else:
        return damageDealt

# If a character's health is below 0, it is returned to 0.
def health_underflow_test(health):
    if health < 0:
        return 0
    else:
        return health

# The sequence for when the user is attacking. The player chooses the stance they will use for the next sequence, applying debuffs or buffs where appropriate.
def combat_attack(enemyHealth, enemyEvade):
    while True:
        combatAction = input('''Would you like to ready your weapon for a power attack (lowering your guard), raise your guard and prepare to block (lowering your power), or keep a balance? Please type Attack, Defend, or Neutral ''' )
        print()
        if combatAction.lower() not in list(['attack', 'a', 'defend', 'd', 'neutral', 'n']):
            print()
            print('That is not a valid input.')
            print()
        else:
            break
    if combatAction.lower() == 'a' or 'attack':
        stance = 'attack'
    elif combatAction.lower() == 'd' or 'defend':
        stance = 'defend'
    else:
        stance = 'neutral'
    if evade_check(enemyEvade):
        print('The enemy evaded your attack.')
        return enemyHealth, stance
    else:
        damageDealt = damage_calculator(stance, True, None, None)
        enemyHealth = enemyHealth - damageDealt
        print('You dealt the enemy ' + str(damageDealt) + ' damage.')
        enemyHealth = health_underflow_test(enemyHealth)
        return enemyHealth, stance

# Sequence when the user is being attacked. Otherwise similar to the attack function.
def combat_defend(playerHealth, playerEvade, playerStance, minAttack, maxAttack):
    if playerStance == 'attack':
        if evade_check(playerEvade):
            print("You evaded the enemy's attack.")
            return playerHealth
        else:
            damageDealt = damage_calculator(playerStance, False, minAttack, maxAttack)
            playerHealth = playerHealth - damageDealt
            print('The enemy dealt you ' + str(damageDealt) + ' damage.')
            playerHealth = health_underflow_test(playerHealth)
            return playerHealth

#Aggregates all of the other functions and returns the enemy's health, as well as picking the enemy's values based off of the name given.
def combat_full(enemy):
    playerStance = 'neutral'
    if enemy == 'basicGrunt':
        enemyHealth = stats.basicGruntStats['health']
        enemyEvade = stats.basicGruntStats['evade']
        enemySpeed = stats.basicGruntStats['speed']
        enemyMinAttack = stats.basicGruntStats['minAttack']
        enemyMaxAttack = stats.basicGruntStats['maxAttack']
        enemyName = 'Basic Grunt'
    print('You face a ' + enemyName + ' in combat')
    print()
    time.sleep(.5)
    # Adds the enemy's speed and player's speed together, and picks a random integer between 1 and
    # that sum. If the sum is between 1 and the player's speed, then the player attacks first.
    # Otherwise, the enemy attacks first.
    if 1 in list(range(1, stats.playerStats['speed']+1)): 
        print('You manage to get the first strike in.')
        time.sleep(.5)
        print()
        enemyHealth, playerStance = combat_attack(enemyHealth, enemyEvade)
    else:
        print("The Basic Grunt manages to get the first strike in.")
        time.sleep(.5)
        print()
    while stats.playerStats['health'] > 0 and enemyHealth > 0:
        print()
        stats.playerStats['health'] = combat_defend(stats.playerStats['health'], stats.playerStats['evade'], playerStance, enemyMinAttack, enemyMaxAttack)
        time.sleep(.5)
        print()
        if stats.playerStats['health'] == 0:
            break
        enemyHealth, playerStance = combat_attack(enemyHealth, enemyEvade)
        time.sleep(.5)
        print()
    return enemyHealth

print()

# Returns whether or not the player won.
if combat_full('basicGrunt') == 0:
    input('You won the battle! Press the Enter key to quit. ')
else:
    input('You lost the battle. Press the Enter key to quit. ')
    