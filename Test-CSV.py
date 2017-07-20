import csv
import os
import re

final = []
last = []

districtSpecific = ('101 - Kettle Run','102 - Catlett','103 - Casanova','502 - New Baltimore','504 - Vint Hill','201 - Saunders','207 - Spriggs','208 - Hylton','209 - Independent Hill','210 - Penn','305 - Pattie','306 - Washington-reid','307 - Henderson','308 - Montclair','309 - Ashland','310 - Forest Park','602 - Beville','603 - Godwin','605 - Minnieville','608 - Enterprise','609 - King')

pattern = re.compile("\d") #makes a pattern that checks for a digit

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
                if ((rows[0] == 'Fauquier County' or rows[0] == 'Prince William County') and (rows[2].startswith(districtSpecific))):
                    print(rows[2])
                    rows.append(str(f).replace('Virginia_Elections_Database__','').replace('_including_precincts.csv',''))
                    final.append(rows)
                
    for rowss in range(len(final)): #This loop makes the INSERT statements for the Precinct Table
        if len(precinctSep(final[rowss][2])) == 2:
            last.append("INSERT INTO Precincts VALUES ('" + str((precinctSep(final[rowss][2]))[1]) + "' , '" + (precinctSep(final[rowss][2]))[0] + "', '" + final[rowss][0].replace(" ","_") + "', " + str(final[rowss][3]).replace(',','') +", " + str(final[rowss][4]).replace(',','') +", " + str(final[rowss][5]).replace(',','') + ", " + str(final[rowss][6]).replace(',','') + ", '" + final[rowss][7] +"' );" )

        elif not (pattern.match(final[rowss][4])): #This condition removes useless information
            pass

        else:
            last.append("INSERT INTO Precincts VALUES ( 'NA' , 'NA' , '" + final[rowss][0].replace(" ","_") + "'," + str(final[rowss][3]).replace(',','') +", " + str(final[rowss][4]).replace(',','') +", " + str(final[rowss][5]).replace(',','') +", " + str(final[rowss][6]).replace(',','') + ", '" + final[rowss][7] + "' );" )


print( "CREATE TABLE Precincts (PrecinctNames varchar(255), PrecinctID varchar(255), ParentCounty varchar(255), Republican int, Democrat int, OtherVotes int, TotalVotesCast int, FileName varchar(255));")
for x in last:
    print (x)


                    
