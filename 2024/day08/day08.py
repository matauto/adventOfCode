#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:13 December 2024
#Time:14:10
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day08.py',
        description = 'advent of code problem solver',
        epilog = 'none')
parser.add_argument("file",
                    default = ".",
                    type = Path,
                    help = "input file for script")
parser.add_argument("part",
                    default = "0",
                    type = int,
                    help = "input file for script")
args = parser.parse_args()

def main():
    fileName=Path(args.file)
    partExec=args.part
    if (fileName.exists() and fileName.is_file()):
        if partExec==0 or partExec==1:
            #solution for first part of puzzle
            print("PART ONE")
            result=0
            inputFile = open(fileName, 'r', encoding="utf-8")
            #scan a file and create dictionary with positions for each node frequency
            #antennaPos=['A':[(x1,y1),...], 'O':[(x2,y2), ...]]
            maxRow=0
            maxCol=0
            antennaPos={}
            for line in inputFile:
                col=0
                for colChar in line:
                    if not(colChar == '.' or colChar == '\n'):
                        if colChar in antennaPos:
                            antennaPos[colChar].append((maxRow,col))
                        else:
                            antennaPos[colChar]=[(maxRow,col)]
                    if not colChar == '\n':
                        col += 1
                if maxCol==0:
                    maxCol = col
                maxRow += 1
            print("antennas positions: ", antennaPos)

            #create dictionary with antinodes for each frequency
            antinodePos={}
            for freq in antennaPos:
                for antPos in antennaPos[freq]:
                    for antPos2 in antennaPos[freq]:
                        if antPos != antPos2:
                            antR = antPos[0]-(antPos2[0]-antPos[0])
                            antC = antPos[1]-(antPos2[1]-antPos[1])
                            if antR >=0 and antC>=0 and antR<maxRow and antC<maxCol:
                                if freq in antinodePos:
                                    antinodePos[freq].append((antR,antC))
                                else:
                                    antinodePos[freq]=[(antR,antC)]

            print("antinodes: ", antinodePos)
            #antinodes have repetitions for position in each frequency
            #it is needed to count only unique positions, for this we need
            #reduce above result to map only occupied positions on map
            #populate map with "."
            antinodeMap=[['.' for col in range(maxCol)] for row in range(maxRow)]
            #put "#" for antinode on map
            for row in range(maxRow):
                for col in range(maxCol):
                    for freq in antinodePos:
                        if (row,col) in antinodePos[freq]:
                            result += 1
                            antinodeMap[row][col]='#'
                            break
                    print(antinodeMap[row][col], end="")
                print("")

            #print("maxRow: ", maxRow, " maxCol: ", maxCol)
            print("Part one answear: ", result)

        if partExec==0 or partExec==2:
            #solution for second part of puzzle 
            print("PART TWO")

            print("Part two answear: ", result)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
