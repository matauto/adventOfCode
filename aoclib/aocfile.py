#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Mateusz O.
#Date:28 December 2024

#load file as 2D array of chars
def file2Dstr(filePath):
    outList=list([])
    with open(filePath, 'r', encoding="utf-8") as inputFile:
        for line in inputFile:
            row=list([])
            for char in line:
                if char != "\n":
                    row.append(char)
            outList.append(row)
    return outList

#load file as 2D array of ints
def file2Dint(filePath):
    outList=list([])
    with open(filePath, 'r', encoding="utf-8") as inputFile:
        for line in inputFile:
            row=list([])
            for char in line:
                if char != "\n":
                    row.append(int(char))
            outList.append(row)
    return outList

#sort the file in form of dictionary with characters and they positions on map
#output={'A':[(x1,y1),...], 'O':[(x2,y2), ...]}
def fileToDict(filePath):
    outputDict={}
    with open(filePath, 'r', encoding="utf-8") as inputFile:
        row=0
        for line in inputFile:
            col=0
            for colChar in line:
                if not(colChar == '\n'):
                    if colChar in outputDict:
                        outputDict[colChar].append((row,col))
                    else:
                        outputDict[colChar]=[(row,col)]
                    col += 1
            row += 1
    return outputDict
def main():# {{{
    print("")

if __name__ == "__main__":
    main()# }}}
