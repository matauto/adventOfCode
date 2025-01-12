#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Mateusz O.
#Date:28 December 2024

#transform 2D map into dict
def toDict(map2D):
    print("use aoclib.file.fileToDict(filePath)")

#class for player moving on the map
class CPlayer:
    def __init__(self, map2D,actPos):
        self.map2D=map2D
        self.actPos=actPos
        self.maxRow=len(map2D)
        self.maxCol=len(map2D[0])
        #overwrite when needed
        self.moveDir={"^":(-1,0),"v":(1,0),">":(0,1),"<":(0,-1)}
    #check if position is inside map
    def insideMap(self, simPos):
        if simPos[0]>=0 and simPos[1]>=0 and simPos[0]<self.maxRow and simPos[1]<self.maxCol:
            return True
        else:
            return False
    #this function return matrix with souroundings of actual position
    #return: [[(),(),()],
    #        [(),actPos.value,()],
    #        [(),(),()],
    def getViewAround(self):
        matrixPos=[[(-1,-1),(-1,0),(-1,1)],[(0,-1),(0,0),(0,1)],[(1,-1),(1,0),(1,1)]]
        outView=list([])
        for row in matrixPos:
            tempRow=list([])
            for addPos in row:
                simPos=(self.actPos[0]+addPos[0],self.actPos[1]+addPos[1])
                tempRow.append(self.getValueMap(simPos))
            outView.append(tempRow)
        return outView

    #this function return matrix with souroundings of actual position
    #return: [(above),(right),(down),(left)]
    def getView4way(self):
        matrixPos=[(-1,0),(0,1),(1,0),(0,-1)]
        outView=list([])
        for addPos in matrixPos:
            simPos=(self.actPos[0]+addPos[0],self.actPos[1]+addPos[1])
            outView.append(self.getValueMap(simPos))
        return outView

    #get values of actual position row as a dict
    #outView={(fromRow,0):'',....,(fromRow,mapSize[1]):''}
    def getViewRow(self,fromRow):
        outView={}
        for col in range(self.maxCol):
            outView[(fromRow,col)]=self.map2D[fromRow][col]
        return outView

    #get values of actual position col as a dict
    #outView={(0,fromCol):'',....,(mapSize[0],fromCol):''}
    def getViewCol(self,fromCol):
        outView={}
        for row in range(self.maxRow):
            outView[(row,fromCol)]=self.map2D[row][fromCol]
        return outView

    #set the new values for elements given in form of dictionary 
    #inputDict={(x,y):'v',...}
    def setMapValues(self,inputDict):
        if inputDict:
            for key,value in inputDict.items():
                if self.insideMap(key):
                    self.map2D[key[0]][key[1]]=value
                else:
                    print("CPlayer.setMapValues class: not in map2D: ", key)

    #check if character is inside a actual view
    #return a list of positions relative to actual position or absolute on map
    def isInsideViewAround(self, matchCharacter, outputRelative):
        outList=list([])
        matrixPos=[[(-1,-1),(-1,0),(-1,1)],[(0,-1),(0,1)],[(1,-1),(1,0),(1,1)]]
        for row in matrixPos:
            for addPos in row:
                simPos=(self.actPos[0]+addPos[0],self.actPos[1]+addPos[1])
                if self.getValueMap(simPos)==matchCharacter:
                    if outputRelative:
                        outList.append(addPos)
                    else:
                        outList.append(simPos)
            outList.append(tempRow)
        return outList 

    #check if character is inside a actual view
    #return a list of positions relative to actual position or absolute on map
    def isInsideView4way(self, matchCharacter, outputRelative):
        outList=list([])
        matrixPos=[(-1,0),(0,1),(1,0),(0,-1)]
        for addPos in matrixPos:
            simPos=(self.actPos[0]+addPos[0],self.actPos[1]+addPos[1])
            if self.getValueMap(simPos)==matchCharacter:
                if outputRelative:
                    outList.append(addPos)
                else:
                    outList.append(simPos)
        return outList

    def makeMove(self, direction):
        if direction in self.moveDir:
            nextPos=self.actPos + self.moveDir[direction]
            #check if nextPos is inside the map
            #if nextPos[0]>=0 and nextPos[1]>=0 and nextPos[0]<self.maxRow and nextPos[1]<self.maxCol:
            if self.insideMap(nextPos):
                self.actPos=nextPos
        return self.actPos

    def setPos(self, nextPos):
        #check if nextPos is inside the map
        if nextPos[0]>=0 and nextPos[1]>=0 and nextPos[0]<self.maxRow and nextPos[1]<self.maxCol:
            self.actPos=nextPos
        return self.actPos
    #get value for any position in map
    def getValueMap(self, simPos):
        if self.insideMap(simPos):
            return self.map2D[simPos[0]][simPos[1]]
        else:
            return ""
    #get a value for actual position
    def getValue(self):
        return sefl.map2D[self.actPos[0]][self.actPos[1]]

    #print a map in elegant way
    def mapPrint(self):
        for row in range(self.maxRow):
            for col in range(self.maxCol):
                print(self.map2D[row][col],end="")
            print("")

def main():# {{{
    print("")

if __name__ == "__main__":
    main()# }}}
