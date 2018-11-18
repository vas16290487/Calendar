import json

def printEntry(entry):
    date = (entry['day'] + '/' + entry['month'] + '/' + entry['year'])
    time = (entry['hour'] + ":" + entry['minute'])
    finalPrint = ("Event Details: " + entry['data'] + "\nOn " + date + " at " + time)
    print(finalPrint + "\n")

with open("./Generic.json", 'r+') as fileToRead:
    entries = json.load(fileToRead)

for entry in entries:
    printEntry(entry)
