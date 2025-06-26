# Jaelee Hutchinson
# 02 Prove: Calling Functions
import math

# import datetime
from datetime import datetime
currentDateTime = datetime.now()

# user input
w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ration of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# calculate volume
v = ((math.pi * (w ** 2) * a) * (w * a + (2540 * d))) / 10000000000

# print
print()
print(f'The approximate volume is {v:.2f} liters')

# extra - ask user to buy tires
choice = input('Would you like to buy tires with these dimensions? (y/n): ')
if  choice == 'y':
    # ask for user's phone number
    phone = input('Please enter your phone number: ')
    # open file
    with open("volumes.txt", "at") as volumesFile:
        print(f'{currentDateTime}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}', file = volumesFile)
        print(f'{phone}', file = volumesFile)
else:
    # open file
    with open("volumes.txt", "at") as volumesFile:
        print(f'{currentDateTime:%Y-%m-%d}', file = volumesFile, end = ', ')
        print(f'{w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}', file = volumesFile)



