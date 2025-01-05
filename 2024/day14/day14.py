#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:04 January 2025
#Time:19:44
#{{{import and argument parser
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path
from collections import Counter

parser = argparse.ArgumentParser(
        prog = 'day14.py',
        description = 'advent of code problem solver',
        epilog = 'none')
parser.add_argument("file",
                    default = ".",
                    type = Path,
                    help = "input file for script")
parser.add_argument("part",
                    default = "0",
                    type = int,
                    choices=[0,1,2],
                    help = "input file for script")
args = parser.parse_args()
#}}}
#{{{functions
class CRobot:
    def __init__(self,mapSize,initPos,velVector):
        self.actPos=initPos
        self.velVec=velVector
        self.mapSize=mapSize
    def moveRobot(self):
        nextPos=self.actPos
        nextPos[0]=self.actPos[0]+self.velVec[0]
        nextPos[1]=self.actPos[1]+self.velVec[1]

        if nextPos[0]>=self.mapSize[0]:
            nextPos[0]-=self.mapSize[0]
        if nextPos[0]<0:
            nextPos[0]+=self.mapSize[0]
        if nextPos[1]>=self.mapSize[1]:
            nextPos[1]-=self.mapSize[1]
        if nextPos[1]<0:
            nextPos[1]+=self.mapSize[1]

        self.actPos[0]=nextPos[0]
        self.actPos[1]=nextPos[1]

def printMap(mapSize,robotPositions):
    positionCounter=Counter(robotPositions)
    for row in range(mapSize[0]):
        for col in range(mapSize[1]):
            if (row,col) in positionCounter:
                print(positionCounter[(row,col)], end="")
            else:
                print(".", end="")
        print("")

def safetyFactor(mapSize,robotsPositions):
    #quarters:
    #1|2
    #4|3
    hr=int((mapSize[0]-1)/2)
    hc=int((mapSize[1]-1)/2)
    count=list([0,0,0,0])
    for robot in robotsPositions:
        r=robot[0]
        c=robot[1]
        if r<hr and c<hc:
            #1 quarter
            count[0]+=1
        elif r<hr and c>hc:
            #2 quarter
            count[1]+=1
        elif r>hr and c>hc:
            #3 quarter
            count[2]+=1
        elif r>hr and c<hc:
            #4 quarter
            count[3]+=1
    return count[0]*count[1]*count[2]*count[3]

def clearScreen():
    print("\033[2J")
#}}}
#{{{solve Part One
def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    robotsList=list([])
    #p=0,4 v=3,-3
    regComp=re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    #user input for map size
    userInput1=input("Map size width: ")
    userInput2=input("Map size height: ")
    timeInput=int(input("Simulation time: "))
    mapSize=(int(userInput2),int(userInput1))
    with open(fileName, 'r', encoding="utf-8") as inputFile:
        for line in inputFile:
            #process the input file
            regSearch=re.search(regComp,line)
            if regSearch:
               rp1=int(regSearch.group(1))
               rp2=int(regSearch.group(2))
               rv1=int(regSearch.group(3))
               rv2=int(regSearch.group(4))
               robotsList.append(CRobot(mapSize,[rp2,rp1],[rv2,rv1]))
               print(f"Robot at position(row,col) ({rp2},{rp1}) velocity ({rv2},{rv1})")

    for seconds in range(timeInput+1):
        posList=list([])
        for robot in robotsList:
            posList.append((robot.actPos[0],robot.actPos[1]))
            robot.moveRobot()
        if seconds ==0:
            print("\nInitial state: ")
        else:
            print("\nState after ",seconds," seconds:")
        printMap(mapSize,posList)
    result=safetyFactor(mapSize,posList)
    print("Part one answear: ", result)

#}}}
#{{{solve Part Two
def solvePartTwo(fileName):
    #solution for second part of puzzle
    print("PART TWO")
    result=0

    print("Part two answear: ", result)
#}}}
#{{{main
def main():
    fileName=Path(args.file)
    partExec=args.part
    if (fileName.exists() and fileName.is_file()):
        if partExec==0 or partExec==1:
            #solution for first part of puzzle
            solvePartOne(fileName)
        if partExec==0 or partExec==2:
            #solution for second part of puzzle 
            solvePartTwo(fileName)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
#}}}
