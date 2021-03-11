#!/bin/python3
import random


COLUMNS = ['A', 'B', 'C', 'D', 'E'];


def printFloorStacks(totalFloors, floorSideLength):
    objectiveTiles = 2 #Safe and Stairs
    locTilesPerFloor = (floorSideLength ** 2) - objectiveTiles 

    availableFloorSpots = []
    for floor in range(1,totalFloors+1):
        availableFloorSpots.extend(
            [floor for _ in range(locTilesPerFloor)])
    random.shuffle(availableFloorSpots)

    for i in range(0, len(availableFloorSpots), totalFloors+1):
            print(availableFloorSpots[i:i+totalFloors+1])


def floorLoc(numberIndex):
    row, colNumber = divmod(numberIndex, 4)
    return COLUMNS[colNumber] + str(row + 1)
    

def getShuffledLocs():
    shuffledIndices = random.sample(list(range(16)), 16)
    shuffledLocs = map(floorLoc, shuffledIndices)
    return list(shuffledLocs)


def printFloorLine():
    print('|---------|---------|---------|')


def printFloorsTable(floorMaps):
    printFloorLine()
    print('| Floor 1 | Floor 2 | Floor 3 |')
    printFloorLine()

    for i in range(16):
        for floor in range(1,4):
            tileLoc = floorMaps.get(floor)[i]
            tileLocFormatted = '|    ' + tileLoc + '   '
            print(tileLocFormatted, end='')
        print('|')

        if((i+1)%4 == 0):
            printFloorLine()


print('Sort Tiles by Floor')
printFloorStacks(3,4)

floorMaps = {}
for floor in range(1,4):
    floorMaps.update({floor: getShuffledLocs()})

print('\n')

printFloorsTable(floorMaps)
