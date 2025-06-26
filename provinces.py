# Jaelee Hutchinson
# 09 Individual Checkpoint

def main():
    # read province list
    provinceList = readList("provinces.txt")
    # print list
    print(provinceList)
    # count Alberta
    for i in range(len(provinceList)):
        if provinceList[i] == "AB":
            provinceList[i] = "Alberta"

    count = provinceList.count("Alberta")

    # print output
    print()
    print(f"Alberta occurs {count} times in the list")


# read provinces list
def readList(filename):
    provinceList = []

    # open provinces text file
    with open (filename) as textFile:
        for line in textFile:
            # remove spaces
            noSpace = line.strip()
            provinceList.append(noSpace)

    return provinceList


# call main
main()