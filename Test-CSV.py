import csv
final = []

with open("Testing.csv", newline='') as thing:
    redy = csv.reader(thing)
    for x in redy:
        final.append(x)
    print (final)
