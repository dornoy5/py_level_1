# # two ways to use packages and modules

# #1) import a package.specific module to get the functions from the module, then call the functions
# from ecommerce.shipping import calc_shipping
# calc_shipping()

# from python_begin.converter import kg_to_lbs, lbs_to_kg

# kg_to_lbs(105)
# lbs_to_kg(234)


# #2) import a package to get a module then call the functions from the module by using the module
# from ecommerce import shipping
# from python_begin import converter
# converter.lbs_to_kg(105)
# shipping.calc_shipping()

# # usin a build package in python
# import random

# for num in range(3):
#     print(random.randint(10,20))
    
# siblings = ["dor", "adi", "enav", "dana"]
# smarter=random.choice(siblings)
# print(smarter)

from games.roll_dice import dice_roll
dice_roll()
 