import random

# for key, value in kwargs:
#    setattr(self, key, value)
#  Consider using this so that you don't have to check
# for so many stats (attributes)
# Remember that you can use dict.get() method so that you don't
# have to check if a key-value pair exists.  If it doesn't,
# it'll default to whatever the second argument is.
# Example, goblin.get('magic', 2) will give 2

# essentially just refer to Chapter 5 in automate


class Combat:
    def __init__(self, kwargs):
        self.action = None
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.current_hp = self.max_hp

    #        self.health = kwargs["health"]
    #        self.min_dmg = kwargs["min_dmg"]
    #        self.max_dmg = kwargs["max_dmg"]
    #        self.armor = kwargs["armor"]
    #        self.dodge = kwargs["dodge"]

    def show_stats(self):
        print(vars(self))

    def attack(self, enemy):
        enemy.take_damage(random.randint(self.min_dmg, self.max_dmg))

    def take_damage(self, damage):
        self.current_hp -= damage


def turn_order():
    pass


def battle(party, enemies):
    pass


if __name__ == "__main__":
    goblin = {"max_hp": 20,
              "min_dmg": 1,
              "max_dmg": 3,
              "armor": 0,
              "dodge": 0,
              "speed": 1,
              "group": "enemy"
              }

    human = {"max_hp": 30,
             "min_dmg": 2,
             "max_dmg": 4,
             "armor": 0,
             "dodge": 0,
             "speed": 2,
             "group": "party"
             }
