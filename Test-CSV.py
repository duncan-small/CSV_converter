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
def precinctSep(precRow):
    precRow = precRow.split("-",1)
    for temp in range(len(precRow)):
        precRow[temp] = precRow[temp].strip()
    return precRow
with open("Testing.csv", newline='') as thing:
    baseData = csv.reader(thing)
    for rows in baseData:
        while (len(rows) != 7):
            rows.append('')
        final.append(rows)
    for rowss in range(len(final)):
        #print (precinctSep(final[rowss][2]))
        if rowss <= 1 or rowss == (len(final) - 1):
            pass
        elif len(precinctSep(final[rowss][2])) == 2:
            print ("INSERT INTO Precincts VALUES (" , (precinctSep(final[rowss][2]))[1] , "," , (precinctSep(final[rowss][2]))[0] , "," , final[rowss][0] , ")" )
        else:
            print ("INSERT INTO Precincts VALUES (" , (precinctSep(final[rowss][2])) , "," , (precinctSep(final[rowss][2])) , "," , final[rowss][0] , ")" )
    for rowNew in range(len(final)):
        for column in range(len(final[rowNew])):
            sortDict[column].append(final[rowNew][column])
    
            
            
