# Jaelee 
# 04 Team Activity: Writing Functions

import math

# main function
def main():
    # lists
    name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z",
        "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40,
        6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 
        7.62, 17.78, 12.38, 11.27, 11.11]
    volumeList = []
    surfaceAreaList = []
    storageEfficiencyList = []


    # call functions
    for x in range(0, len(radius)): 
        volume = computeVolume(radius[x], height[x])
        volumeList.append(volume)

    for x in range(0, len(radius)):
        surfaceArea = computeSurfaceArea(radius[x], height[x])
        surfaceAreaList.append(surfaceArea)

    for x in range(0, len(volumeList)):
        storageEfficiency = computeStorageEfficiency(volumeList[x], surfaceAreaList[x])
        storageEfficiencyList.append(storageEfficiency)

    
    # print
    for x in range(0, len(name)):
        print(f'{name[x]} {storageEfficiencyList[x]:.2f}')

# compute volume
def computeVolume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


# compute surface area
def computeSurfaceArea(radius, height):
    surfaceArea = 2 * math.pi * radius * (radius + height)
    return surfaceArea


# compute storage efficiency
def computeStorageEfficiency(volume, surfaceArea):
    storageEfficiency = volume / surfaceArea
    return storageEfficiency


# call main to start
main()
