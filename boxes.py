# Jaelee Hutchinson
# 02 Checkpoint: Calling Functions

import math

# user input
items = int(input('Enter the number of items: '))
itemsPer = int(input('Enter the number of items per box: '))

# calculation
boxes = items / itemsPer

# print
print(f'For {items} items, packing {itemsPer} items in each box, you will need {math.ceil(boxes)} boxes.')

