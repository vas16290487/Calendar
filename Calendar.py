class Entry(object):
    #This allows for quicker access of each entry's fields
    __slots__= 'day','month','year','data','comment','TEMPline'
    def __init__(self,line):
        #This line will eventually handle each part of the data
        self.day = self.month =self.year = self.data = self.comment = "DEFAULT"
        self.TEMPline = line

entries = []

#Begin file extraction
with open("./generic", 'r+') as fileToRead:
    for line in fileToRead:
        entries.append(Entry(line))
print(entries[0].TEMPline)
print(entries[1].TEMPline)
print(entries[2].TEMPline)
print(entries[3].TEMPline)
