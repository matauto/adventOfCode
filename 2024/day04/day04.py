#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author: Mateusz O.
#Date:04 December 2024
#Time:23:45
#based on Advent Of Code template from github.com/matauto/templates

import argparse
import sys
import os
import re
from pathlib import Path

parser = argparse.ArgumentParser(
        prog = 'day04.py',
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
        inputFile = open(fileName, 'r', encoding="utf-8")
        
        if partExec==0 or partExec==1:
            print("PART ONE")
            #fullFile = inputFile.read()

            #word to find XMAS
            #horizontal normal
            hn = re.compile("XMAS")
            #hnL = hn.findall(fullFile)
            #horizontal backward
            hb = re.compile("SAMX")
            #hbL = hb.findall(fullFile)
            #line buffers
            lineBuf1=[]
            lineBuf2=[]
            lineBuf3=[]
            #temp to normalize to horizontal form
            tempVert=""
            tempDiagR=""
            tempDiagL=""
            result=0
            iteration=0
            #PROCESS FILE
            for line in inputFile:
                #print(line)
                #find horizontal normal in line
                hnL = hn.findall(line)
                result = result + len(hnL)
                if hnL:
                    print("hnL", hnL)
                #find horizontal bacward in line
                hbL = hb.findall(line)
                result = result + len(hbL)
                if hbL:
                    print("hbL", hbL)
                #for vertical and diagonal
                #scan will be performed and transformation
                #to horizontal form to do this we need 4 lines matrix
                if lineBuf1 and lineBuf2 and lineBuf3:
                    for i in range(len(line)):
                        tempVert=lineBuf3[i]+lineBuf2[i]+lineBuf1[i]+line[i]
                        if tempVert=="XMAS" or tempVert=="SAMX":
                            result=result+1
                            print("Vert: ", tempVert)
                    for i in range(0,(len(line)-3)):
                        tempDiagR=lineBuf3[i+3]+lineBuf2[i+2]+lineBuf1[i+1]+line[i]
                        #print(tempDiagR)
                        if tempDiagR=="XMAS" or tempDiagR=="SAMX":
                            result=result+1
                            print("DiagR: ", tempDiagR)
                    for i in range(3,(len(line))):
                        tempDiagL=lineBuf3[i-3]+lineBuf2[i-2]+lineBuf1[i-1]+line[i]
                        #print(tempDiagL)
                        if tempDiagL=="XMAS" or tempDiagL=="SAMX":
                            result=result+1
                            print("DiagL: ", tempDiagL)
                #iterate buffers
                lineBuf3=lineBuf2
                lineBuf2=lineBuf1
                lineBuf1=line
            #solution for first part of puzzle
            print("Part one answear: ", result)

        if partExec==0 or partExec==2:
            print("PART TWO")
            result=0
            #solution for second part of puzzle 

            print("Part two answear: ", result)
    else:
        print("it is not file")

if __name__ == "__main__":
    main()
