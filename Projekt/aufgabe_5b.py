import sys
import csv
import math
from collections import Counter

import aufgabe_5a

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

def getDocWithMaxRating(dictTf, dictIdf, searchText):
    dictDocRanking = getRatingList(dictTf, dictIdf, searchText)
    return max(dictDocRanking, key=dictDocRanking.get)

def getRatingList(dictTf, dictIdf, searchText):
    dictQuery = {}
    dictDocVector = {}
    termFreq = {}
    dictDocRanking = {}
    searchwords = aufgabe_5a.stringNormalizer(searchText)

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
            dictQuery[term] = math.log((len(dictTf) + 1) / (termFreq[term] + 1)) * float(swrFreq[term] / maxVal)

    for document in dictDocVector:
        dictDocRanking[document] = sim(dictDocVector[document], dictQuery)

    return dictDocRanking

def getIdf(idffilename):
    dictIdf = {}
    with open(idffilename, 'r', encoding="utf-8") as csvfile:
        idfreader = csv.reader(csvfile)
        for row in idfreader:
            dictIdf[row[0]] = row[1]

    return dictIdf

def getTf(tffilename):
    dictTf = {}
    with open(tffilename, 'r', encoding="utf-8") as csvfile:
        tfreader = csv.reader(csvfile)
        for row in tfreader:
            docName = row.pop(0)
            dictTf[docName] = dict()
            while len(row) > 0:
                freq = row.pop()
                word = row.pop()
                dictTf[docName][word] = freq
    return dictTf


#Starts here
if __name__ == "__main__":
    searchwords = []

    tffilename = "data/tf.csv"
    if len(sys.argv) > 1:
        tffilename = sys.argv[1]

    idffilename = "data/idf.csv"
    if len(sys.argv) > 2:
        idffilename = sys.argv[2]

    if len(sys.argv) > 3:
        with open(sys.argv[3], encoding="utf-8") as swfile:
            searchwords = swfile.read()

    if len(searchwords) == 0:
        searchwords = input("Enter search string: ")

    if len(searchwords) == 0:
        dictIdf = getIdf(idffilename)
        dictTf = getTf(tffilename)

        with outputfile_open() as outfile:
            outfile.write(getDocWithMaxRating(dictTf, dictIdf, searchwords))
