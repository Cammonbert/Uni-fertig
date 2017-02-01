import sys
import csv
import math
from collections import Counter

def outputfile_open():
    try:
        if len(sys.argv) > 4:
            fh = open(sys.argv[4], "w", encoding="utf-8")
        else:
            fh = sys.stdout
        return fh
    except IOError:
        print("Error: could not open output file for writing!")

def sim(q, d):
    retVal = 0.0
    for t in q:
        if t in d:
            retVal += q[t] * d[t]
    vecMod = 0
    for word in d:
        vecMod += d[word] * d[word]
    vecMod = math.sqrt(vecMod)
    retVal /= vecMod
    return retVal

#Starts here
searchwords = []
dictIdf = {}
dictTf = {}
termFreq = {}
dictDocVector = {}
dictQuery = {}
dictDocRanking = {}

tffilename = "tf.csv"
if len(sys.argv) > 1:
    tffilename = sys.argv[1]

idffilename = "idf.csv"
if len(sys.argv) > 2:
    idffilename = sys.argv[2]

if len(sys.argv) > 3:
    with open(sys.argv[3], encoding="utf-8") as swfile:
        searchwords = swfile.read().split(" ")

if len(searchwords) == 0:
    eingabe = ""
    while eingabe != " ":
        eingabe = input("Enter search string: ")
        if eingabe != " ":
            searchwords += eingabe.split(" ")

with open(idffilename, 'r', encoding="utf-8") as csvfile:
    idfreader = csv.reader(csvfile)
    for row in idfreader:
        dictIdf[row[0]] = row[1]

with open(tffilename, 'r', encoding="utf-8") as csvfile:
    tfreader = csv.reader(csvfile)
    for row in tfreader:
        docName = row.pop(0)
        dictTf[docName] = dict()
        while len(row) > 0:
            freq = row.pop()
            word = row.pop()
            dictTf[docName][word] = freq

for document in dictTf:
    dictDocVector[document] = dict()
    for term in dictTf[document]:
        dictDocVector[document][term] = (float(dictTf[document][term]) * float(dictIdf[term]))
        termFreq[term] = termFreq.get(term, 0) + 1

'''
 Create vector for query
  Number of all documents for query = Number of all documents + 1
  number of documents that contain term for query = number of documents that contain term + 1
  number of times term occurs in doc for query = number of times term occurs in doc + 1
  maxOccurrences = maxOccurrences
'''
swrFreq = Counter(searchwords)
maxVal = max(swrFreq.values())

for term in searchwords:
    if term in termFreq:
        dictQuery[term] = math.log((len(dictTf) + 1)/ (termFreq[term] + 1)) * float(swrFreq[term] / maxVal)

for document in dictDocVector:
    dictDocRanking[document] = sim(dictDocVector[document], dictQuery)

with outputfile_open() as outfile:
    outfile.write(max(dictDocRanking, key=dictDocRanking.get))
