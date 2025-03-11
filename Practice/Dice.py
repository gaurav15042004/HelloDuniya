import random


class Dice:
    def roll(self):
        i = random.randint(1, 6), random.randint(1, 6)
        print(i)


turn = Dice()
turn.roll()