import csv
import os
import re

final = []
last = []

colOne = []
colTwo = []
colThree = []
colFour = []
colFive = []
colSix = []
colSeven = []

pattern = re.compile("\d") #makes a pattern that checks for a digit

combined = [colOne,colTwo,colThree,colFour,colFive,colSix,colSeven]
sortDict = {0:colOne,1:colTwo,2:colThree,3:colFour,4:colFive,5:colSix,6:colSeven}

def precinctSep(precRow): #This function seperates the precinct name from the id, the original format is "id - name", I make it a list : [name,id]

    precRow = precRow.split("-",1) #breaks the string where there is a dash and puts it into a list

    for temp in range(len(precRow)):
        precRow[temp] = precRow[temp].strip().replace(" ","_") #this takes out spaces from both sides and turns the remaining into underscores to fit SQL Syntax

    return precRow
indir = 'Data/'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        with open(os.path.join(root, f), newline='') as thing:
            
            baseData = csv.reader(thing)
            
            for rows in baseData: #This loop makes the main file a more standard list called 'final'

                while (len(rows) != 7):
                    rows.append('')

                final.append(rows)
            for rowss in range(len(final)): #This loop makes the INSERT statements for the Precinct Table

                if not (pattern.match(final[rowss][4])): #This condition removes useless information
                    pass
                
                elif len(precinctSep(final[rowss][2])) == 2:
                    last.append("INSERT INTO Precincts VALUES ('" + str((precinctSep(final[rowss][2]))[1]) + "' , '" + (precinctSep(final[rowss][2]))[0] + "', '" + final[rowss][0].replace(" ","_") + "', " + str(final[rowss][3]).replace(',','') +", " + str(final[rowss][4]).replace(',','') +", " + str(final[rowss][5]).replace(',','') + ", " + str(final[rowss][6]).replace(',','') + ',' + f +" );" )

                else:
                    last.append("INSERT INTO Precincts VALUES ( 'NA' , 'NA' , '" + final[rowss][0].replace(" ","_") + "'," + str(final[rowss][3]).replace(',','') +", " + str(final[rowss][4]).replace(',','') +", " + str(final[rowss][5]).replace(',','') +", " + str(final[rowss][6]).replace(',','') + ',' + f + " );" )

            
    print( "CREATE TABLE Precincts (PrecinctNames varchar(255), PrecinctID varchar(255), ParentCounty varchar(255), Republican int, Democrat int, OtherVotes int, TotalVotesCast int, FileName varchar(255));")
    for x in last:
        print (x)


                    
