import random 

# def dice_roll():
#         for i in range(1):
#             dice1= random.randint(1,6)
#             dice2= random.randint(1,6)
#             print(f"({dice2},{dice1})")
            
class Dice:
    def dice_roll(self):
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        return dice1 , dice2

print(Dice().dice_roll())   
