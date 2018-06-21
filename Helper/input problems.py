def player_input():
     while True:
        l = input("Choose your sign\n x or o\n")
        if l=='x' or l=='o':
            print('Player 1 chose {}'.format(l))
            break
        else:
            print("Wrong sign chosen.Choose between x or o")
player_input()

