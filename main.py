# This program is copied from
# https://realpython.com/python-dice-roll/

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def generate_dice_faces_diagram(dice_value):

    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_value:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        print("row_idx = " + str(row_idx))
        row_components = []
        for die in dice_faces:
            print('die = ' + str(die))
            print("die[row_idx] = " + die[row_idx])
            row_components.append(die[row_idx])
        print('row_components = ' + str(row_components))
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        print('row_string = ' + str(row_string))
        dice_faces_rows.append(row_string)
        print('dice_faces_rows = ' + str(dice_faces_rows))

    # Generate header with the word "RESULT" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    print('dice_faces_diagram = ' + str(dice_faces_diagram))
    return dice_faces_diagram


def roll_dice(num):
    roll_results = []
    for _ in range(num):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def parse_input(num):
    if num in {'1', '2', '3', '4', '5', '6'}:
        return int(num)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


num_dice_input = input("How many dice do you want to roll? [1-6] ")
num_dice = parse_input(num_dice_input)

results = roll_dice(num_dice)

dice_face_diagram = generate_dice_faces_diagram(results)
print(f"\n{dice_face_diagram}")

