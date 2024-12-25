#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#{{{import and argument parser
#Author: Mateusz O.
#Date:22 December 2024
#Time:22:42
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
import time
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day10.py',
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
def getNextPos(hikeMap, currentPos,nextHeight):
    #right,down,left,up
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    retPos=list([])
    for direction in directions:
        nextPos=(currentPos[0]+direction[0],currentPos[1]+direction[1])
        #print(nextPos)
        #check if nextPos is inside the map
        if nextPos[0]>=0 and nextPos[0]<len(hikeMap) and nextPos[1]>=0 and nextPos[1]<len(hikeMap[currentPos[0]]):
            if hikeMap[nextPos[0]][nextPos[1]]==nextHeight:
                retPos.append(nextPos)
    return retPos
#}}}
#{{{solve Part One
def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    #create hikeMap and list of trailheads
    hikeMap=list([])
    trailHeads=list([])
    with open(fileName, 'r', encoding="utf-8") as inputFile:
        for i,line in enumerate(inputFile):
            #process the input file
            row=list([])
            for j,char in enumerate(line):
                if not char=="\n":
                    row.append(int(char))
                if char=="0":
                    trailHeads.append((i,j))
            hikeMap.append(row)

    print("Hike map: ",hikeMap)
    print("Trailheads: ",trailHeads)
    #for each trailhead as start point go up and down to find out all the routes
    #add every(in trailhead context) visited position to set
    for trailHead in trailHeads:
        visitedPos=set({})
        actualPos=trailHead
        actualHeigh=0
        goUp=True
        trailResult=0
        loopTrue=True
        while loopTrue:
            #print(actualPos)
            #check actual heigh
            actualHeight=hikeMap[actualPos[0]][actualPos[1]]
            #next positions for up and down
            nextPositionsUP=getNextPos(hikeMap, actualPos, actualHeight+1)
            nextPositionsDOWN=getNextPos(hikeMap, actualPos, actualHeight-1)
            #print("UP: ", nextPositionsUP, "DOWN: ", nextPositionsDOWN)
            #the condition to end the loop = we are in start position without next place to move
            if actualPos==trailHead and not nextPositionsUP:
                print("Trailhead: ",trailHead," empty. Trails: ", trailResult)
                loopTrue=False
                break
            #if we are at the top ==9 we count this as result and change direction to go down
            if actualHeight==9 and goUp:
                result += 1
                trailResult += 1
                goUp=False
                print("Path to 9 in pos: ",actualPos, " found from ", trailHead)
            #decide if climb up or go down
            if nextPositionsUP:
                lNotVisited=0
                for nextPos in nextPositionsUP:
                    if not (nextPos in visitedPos):
                        goUp=True
                        lNotVisited += 1
                        break
                    else:
                        goUp=False
                if actualPos==trailHead and lNotVisited==0:
                    print("Exit from trailhead: ", trailHead," with result: ", trailResult)
                    loopTrue=False
            elif nextPositionsDOWN:
                goUp=False
            else:
                break
            #add actual position to visited places
            visitedPos.add(actualPos)
            #print("Visited: ", visitedPos)
            #make a move to next position - we take a first position from a list which is
            #not in set with last visited positions if we go up or is if we go dawn
            if nextPositionsUP and goUp:
                for nextPosition in nextPositionsUP:
                    if not (nextPosition in visitedPos):
                        actualPos=nextPosition
                        break
            if nextPositionsDOWN and not goUp:
                for nextPosition in nextPositionsDOWN:
                    if nextPosition in visitedPos:
                        actualPos=nextPosition
                        break
            #time.sleep(0.5)
            #print("For trialhead ", trailHead, " next positions: ", nextPositions)
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
