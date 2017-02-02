import sys

def outputfile_open():
    try:
        if len(sys.argv) > 3:
            fh = open(sys.argv[3], "w", encoding="utf-8")
        else:
            fh = sys.stdout
        return fh
    except IOError:
        print("Error: could not open output file for writing!")

#Starts here
searchwords = dict()
dictText = dict()

linkstatistikfilename = "data/Linkstatistik.txt"
if len(sys.argv) > 1:
    linkstatistikfilename = sys.argv[1]

if len(sys.argv) > 2:
    with open(sys.argv[2], encoding="utf-8") as swfile:
        for i in swfile:
            searchwords[i.rstrip()] = 0

if len(searchwords) == 0:
    eingabe = ""
    while eingabe != " ":
        eingabe = input("Enter search string: ")
        if eingabe != " ":
            searchwords[eingabe] = 0

with open(linkstatistikfilename, encoding="utf-8") as readfile:
    for i in readfile:
        tuple = i.rstrip().split("\t")
        if len(tuple) > 2:
            if tuple[2] in searchwords:
                if int(tuple[0]) > searchwords[tuple[2]]:
                    searchwords[tuple[2]] = int(tuple[0])
                    dictText[tuple[2]] = tuple[1]

with outputfile_open() as outfile:
    for i in searchwords:
        if i in dictText:
            outfile.write(str(dictText[i]) + "\n")
