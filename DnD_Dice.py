import random
DiceChoises = [4,6,8,10,12,20,100]
Dice = input("Pick a Dice: \n 1 = d4 \n 2 = d6 \n 3 = d8 \n 4 = d10 \n 5 = d12 \n 6 = d20 \n 7 = d100 \n :  ")
HowManyDices = input("How many Dices Do you want to role ? ")
AjustedDiceNumber = int(Dice) - 1
result = int(DiceChoises[AjustedDiceNumber]) * int(HowManyDices) 
rangeoutcome = range(result)
Listoutcome = list(rangeoutcome)
outcome =  random.choice(Listoutcome)
while outcome == 0:
    outcome =  random.choice(Listoutcome)
print(outcome)
