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
with open("Testing.csv", newline='') as thing:
    baseData = csv.reader(thing)
    for rows in baseData:
        while (len(rows) != 7):
            rows.append('')
        final.append(rows)
    for rowNew in range(len(final)):
        for column in range(len(final[rowNew])):
            sortDict[column].append(final[rowNew][column])
    print (combined)
            
            
