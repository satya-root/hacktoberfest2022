import random

def roll_dice():
    numbers = ''
    for i in range(1, 7):
        numbers += str(i)
    selected_num = (random.choice(numbers))
    print(f'Your dice is rolling! You got: {selected_num}')


roll_dice()
