# Jaelee Hutchinson
# 03 Prepare: Writing Functions

import math

# main function
def main():
    # user input
    radius = float(input('Enter the radius of a cylinder: '))
    height = float(input('Enter the height of a cylinder: '))

    # call function for volume
    volume = calcVolume(radius, height)

    # print
    print(f'Volume: {volume:.2f}')


# calculation for volume
def calcVolume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


# call main function
main()