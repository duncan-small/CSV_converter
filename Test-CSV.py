import csv


final = []

colOne = []
colTwo = []
colThree = []
colFour = []
colFive = []
colSix = []
colSeven = []

combined = [colOne,colTwo,colThree,colFour,colFive,colSix,colSeven]
sortDict = {0:colOne,1:colTwo,2:colThree,3:colFour,4:colFive,5:colSix,6:colSeven}

def precinctSep(precRow): #This function seperates the precinct name from the id, the original format is "id - name", I make it a list : [name,id]

    precRow = precRow.split("-",1)

    for temp in range(len(precRow)):
        precRow[temp] = precRow[temp].strip().replace(" ","_")

    return precRow

with open("Testing.csv", newline='') as thing:
    
    baseData = csv.reader(thing)
    
    for rows in baseData: #This loop makes the main file a more standard list called 'final'

        while (len(rows) != 7):
            rows.append('')

        final.append(rows)
    print( "CREATE TABLE Precincts (PrecinctNames varchar(255), PrecinctID varchar(255), ParentCounty varchar(255), LeeScottLingamfelter int,SaraElizabethTownsend int, OtherVotes int, TotalVotesCast int);")    
    for rowss in range(len(final)): #This loop makes the INSERT statements for the Precinct Table

        if rowss <= 1: #This condition removes useless information
            pass
        
        elif len(precinctSep(final[rowss][2])) == 2:
            print ("INSERT INTO Precincts VALUES ('" + str((precinctSep(final[rowss][2]))[1]) + "' , '" + (precinctSep(final[rowss][2]))[0] + "', '" + final[rowss][0].replace(" ","_") + "'," , int(str(final[rowss][3]).replace(',','')) ,"," , int(str(final[rowss][4]).replace(',','')) ,"," , int(str(final[rowss][5]).replace(',','')) ,"," , int(str(final[rowss][6]).replace(',','')) , ");" )

        else:
            print ("INSERT INTO Precincts VALUES ( 'NA' , 'NA' , '" + final[rowss][0].replace(" ","_") + "'," , int(str(final[rowss][3]).replace(',','')) ,"," , int(str(final[rowss][4]).replace(',','')) ,"," , int(str(final[rowss][5]).replace(',','')) ,"," , int(str(final[rowss][6]).replace(',','')) , ");" )



    

    

    for rowNew in range(len(final)):

        for column in range(len(final[rowNew])):

            sortDict[column].append(final[rowNew][column])
    
            
            
