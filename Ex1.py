import pandas as pd
import numpy as np
from Building import Building
from Elevator import Elevator
from CallForElevator import CallForElevator
import json

def LoadCalls(path):
    try:
        calls = pd.read_csv(path)
    except:
        print("ERROR: This is not a CSV file !")

def LoadBuilding(path):
    try:
        with open(path, "r") as f:
            build = json.load(f)
            my_building = Building(build)
            for my_elev in build['_elevators']:
                my_building.elev.append(Elevator(my_elev))
    except:
        print("ERROR: This is not a JSON file !")