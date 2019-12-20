import pandas as pd 
import numpy as np 


def bDay():

    print ("\n==================Welcome to the Birthday Dictionary. We know the Birthdays of:==================\n")
     
    bdayDict = {'Name':['Benjamin Franklin', 'Ada Lovelace', 'Steve Jobs', 'Jack Dorsey','Elon Musk'],
                'Birthday':['01/17/1706', '12/10/1815', '02/24/1955', '11/19/1976', '06/28/1971']}


               
    #use pandas to visualize clean data
    df = pd.DataFrame(bdayDict)

    #prints a list of all the names with birthdays on record
  
    print("\n"+(df['Name']).to_string(index=False)+"\n")

    name = input(str("Please enter the full name to see birthday date or enter 'All' to see everything:"))
    while name != 'END':

        if name == "Benjamin Franklin":
            print(df.iloc[[0], :])
        elif name == "Ada Lovelace":
            print(df.iloc[[1], :])
        elif name == "Steve Jobs":
            print(df.iloc[[2], :])
        elif name == "Jack Dorsey":
            print(df.iloc[[3], :])
        elif name == "Elon Musk":
            print(df.iloc[[4], :])
        elif name == "ALL":
            print(df.to_string(index=False))
        else:
            print("Name entered is not in records")
        name = input(str("\nPlease enter the full name to see birthday date or enter 'All' to see everything or 'END' to quit:"))
bDay()