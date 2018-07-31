class Animal:
    def __init__(self, alive=True):
        self.alive = alive

    def move(self):
        print("I'm walkin', daddy!")


class Mammal(Animal):
    def __init__(self, fur=True, milk=True):
        super().__init__()
        self.fur = fur
        self.milk = milk

    def birth_live_young(self):
        print("Just made myself an alive baby")


if __name__ == "__main__":
    dog = Mammal()
    print(dog.alive)
    dog.move()
    dog.birth_live_young()
