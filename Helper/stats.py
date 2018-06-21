import inventory

# Will be called on when stats are needed
playerStats = {'health': 40, 'maxHealth': 40, 'evade': 5, 'speed': 5, 'minAttack': 1, 'maxAttack': 10+int(inventory.playerInventory['weapon'])}

basicGruntStats = {'health': 40, 'evade': 2, 'speed': 3, 'minAttack': 1, 'maxAttack': 10}
