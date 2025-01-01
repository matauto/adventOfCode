#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:27 December 2024
#Time:20:46
#{{{import and argument parser
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path
#from github.com/matauto/adventOfCode/aoclib
import aoclib as aoc

parser = argparse.ArgumentParser(
        prog = 'day12.py',
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
#}}}
#{{{solve Part One
def solvePartOne(fileName):
    #solution for first part of puzzle
    print("PART ONE")
    result=0
    gardenMap=aoc.file.file2Dstr(fileName)
    gardenMapDict=aoc.file.fileToDict(fileName)
    gardener=aoc.map2D.CPlayer(gardenMap, (0,0))

    #print(gardenMap)
    #print(gardener.getView())
    #loop through each plant(letter) and calculate the area(lenght of letter list) and perimeter(according to neiberhood of letter)
    for plant, areaList in gardenMapDict.items():
        areaRegions=list([])
        areaUnsorted=areaList
        oldLenght=len(areaUnsorted)
        #the same plant could be divided on couple of areas
        index=-1
        loopGuard=-1
        while areaUnsorted:
            #if we iterate trough all garden plots and do not delete nothing from unsorted list we must create a new area
            if loopGuard<0:
                areaRegions.append([areaUnsorted[0]])
                areaUnsorted.remove(areaUnsorted[0])
                index +=1
                loopGuard=len(areaUnsorted)
                continue
            
            #tempList=areaUnsorted
            for gardenPlot in areaUnsorted:
                gardener.setPos(gardenPlot)
                #get a list of given charakter around actual position
                viewList=gardener.isInsideView4way(plant, False)
                #print("viewList: ", viewList)
                if viewList:
                    for view in viewList:
                        if view in areaRegions[index]:
                            #print("delete: ", gardenPlot)
                            areaRegions[index].append(gardenPlot)
                            areaUnsorted.remove(gardenPlot)
                            #add rest from view to area region
                            for view2 in viewList:
                                if not(view2 in areaRegions[index]):
                                    #print("delete: ", view2)
                                    areaRegions[index].append(view2)
                                    areaUnsorted.remove(view2)
                            break
            loopGuard -=1
            #print("area unsorted:",areaUnsorted)
            #print("area regions",areaRegions)
        print("For plant: ",plant, " areas: ", areaRegions)
        for areaRegion in areaRegions:
            perimeter=0
            area=len(areaRegion)
            for gardenPlot in areaRegion:
                gardener.setPos(gardenPlot)
                view=gardener.getViewAround()
                #above
                if not view[0][1]==plant:
                    perimeter += 1
                    #print(view[0][1],gardenPlot,view)
                #right
                if not view[1][2]==plant:
                    perimeter += 1
                #down
                if not view[2][1]==plant:
                    perimeter += 1
                #left
                if not view[1][0]==plant:
                    perimeter += 1
            print("for plant: ",plant," area=",area,"perimeter=",perimeter, " cost=",area*perimeter)
            result += perimeter*area

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
