# rules
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win


import random

def swg(computer, human):
    if (computer == human):
        return None
    elif (computer == "s" and human == "g"):
        return True
    elif (computer == "w" and human == "s"):
        return True
    elif (computer == "g" and human == "w"):
        return True
    else:
        return False


choice = ("s", "w", "g")
computer = random.randint(0, 2)
computer = choice[computer]
human = input("Choose either s || w || g :  ")

win = swg(computer, human)
print(f"You chose: {human}.. AND the computer chose: {computer}..")
if win is None:
    print("Match is Draw")
if win:
    print("----YOU WIN----")
else:
    print("----YOU LOOSE----")