import random

num_sides = 6

def roll_dice():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)

    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")
def main():
    die1 = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()