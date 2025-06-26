# Jaelee Hutchinson
# Final Project
# Random Date Generator
import random


def main():
    # call functions
    count = userInput()
    dates = dateIdeas()  
    printDates(count, dates)



def dateIdeas():
    # create list for dates
    dates = ["Dinner and movie", "Cook together", "Bake cookies", "Rollerskating", "Bowling",
        "Picnic", "Get ice cream", "Karaoke", "Play board games", "Take a walk"]

    return dates



def userInput():
    # ask user how many date ideas they want
    print("Welcome to the Random Date Generator")
    count = int(input("How many date ideas would you like? (1-10): "))

    return count



def randomNumGenerator(dates):
    # chose random date
    chosenDate = random.choice(dates)

    return chosenDate



def printDates(count, dates):
    # print the dates
    print()
    if (count > 1):
        print("Here are your dates!")
    elif (count == 1):
        print("Here is your date!")
    else:
        print("Why don't you want any date ideas? :(")


    if (count == 10):
        for x in dates:
            print(x)
    else:
        while count > 0:
            chosenDate = randomNumGenerator(dates)
            count = count - 1
            print(chosenDate)


# call main
main()