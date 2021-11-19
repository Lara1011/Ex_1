from csv import writer
import pandas as pd
import numpy as np
from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator
import json
import csv

def LoadCalls(path):
    try:
        calls = pd.read_csv(path,header=None)
        return calls
    except:
        print("ERROR: This is not a CSV file !")

def LoadBuilding(path):
    try:
        with open(path, "r") as f:
            build = json.load(f)
            my_building = Building(build)
            for my_elev in build['_elevators']:
                my_building.elev.append(Elevator(my_elev))
            #build.close()
        return my_building
    except:
        print("ERROR: This is not a JSON file !")

def LoadOutput(index, path, row):
    path.loc[row, '5'] = index
    return path

def allocateElevator(path1, path2, path3):
    myBuilding = LoadBuilding(path1)
    myCalls = LoadCalls(path2)
    myOut = LoadCalls(path2)
    print(myOut)
    myOut['difference'] = abs(myOut[2]-myOut[3])
    myOut = myOut.sort_values(['difference'], ascending=True)
    myOut['RunHere'] = range(0,len(myOut))
    myOut = myOut.set_index(['RunHere'])
    numOfElev = len(myBuilding.elev)
    partition = int(len(myOut) / numOfElev)
    if numOfElev == 1:
        for i in myOut.index:
            myOut[5] = myBuilding.elev[0].getID
    else:
        sortElevList = myBuilding.elev
        start = 0
        stop = len(myBuilding.elev)
        for i in range(0,len(myOut),partition):
            if start<stop:
                newvalue = sortElevList[start].getID
                for j in range(i, partition+i):
                  myOut.at[j,5] = start
                # myOut.loc[i:(i+partition -1) ,5] = newvalue
            start = start + 1
    myOut = myOut.drop(['difference'],axis=1)
    myOut.reset_index(drop=True, inplace=True)
    j=0
    k=partition
    for i in myOut:
        while(i<k):
            myBuilding.elev[j].call.append(myOut[2].iloc[i])
            myBuilding.elev[j].call.append(myOut[3].iloc[i])
            i = i+1
        k = k+partition
        j = j+1
        if len(myBuilding.elev)==j:
            break
    myOut = myOut.sort_values([1])
    myOut.to_csv(path3, index=False, header = False)
    print(myOut)


'''''
    # path 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if len(myBuilding.elev)==1:
        for i in myCalls:
            myOut = LoadOutput(myBuilding.elev.getID, myOut, i)
    else:
        for i in myCalls:
            minTime = []
            for j in len(myBuilding.elev):

def sumTillNextCall(elevator, call):
    # check this copy() if works !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    copyList = elevator.call.copy()
    calTime = 0
    for i in copyList:
'''''

if __name__ == '__main__':
    allocateElevator(r'C:\Users\malak\OneDrive\Desktop\New folder\B1.json',
                     r'C:\Users\malak\OneDrive\Desktop\New folder\Calls_a.csv',
                     r'C:\Users\malak\OneDrive\Desktop\New folder\output.csv')