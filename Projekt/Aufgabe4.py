from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import sys
import string

def outputfile_open():
    try:
        if len(sys.argv) > 3:
            fh = open(sys.argv[3], "w")
        else:
            fh = sys.stdout
        return fh
    except IOError:
        print("Error: could not open output file for writing!")

def analyseSentenses(inputList, linkstatistikfilename):
    jar = 'stanford-ner-2016-10-31/stanford-ner.jar'
    model = 'stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz'
    st = StanfordNERTagger(model, jar)

    # create list with words to look up
    searchwords = dict()
    for sentence in inputList:
        sentence = word_tokenize(sentence)
        tags = st.tag(sentence)

        prevtup = ('', '')
        for tup in tags:
            if tup[1] == prevtup[1]:
                if tup[1] != "O":
                    prevtup = (str(prevtup[0] + " " + tup[0]), tup[1])
            else:
                if prevtup[0] != "" and prevtup[1] != "O":
                    searchwords[prevtup[0]] = 0
                prevtup = (tup[0], tup[1])
        if prevtup[0] != "" and prevtup[1] != "O":
            searchwords[prevtup[0]] = 0

    #create ranking
    dictText = dict()
    with open(linkstatistikfilename, encoding="utf-8") as readfile:
        for i in readfile:
            tuple = i.rstrip().split("\t")
            if len(tuple) > 2:
                if tuple[2] in searchwords:
                    if int(tuple[0]) > searchwords[tuple[2]]:
                        searchwords[tuple[2]] = int(tuple[0])
                        dictText[tuple[2]] = tuple[1]

    #create sentense to return
    outputList = list()

    for sentence in inputList:
        sentence = word_tokenize(sentence)
        tags = st.tag(sentence)

        satz = ""
        prevtup = ('', '')
        for tup in tags:
            if tup[1] == prevtup[1]:
                text = prevtup[0]
                if tup[0] not in string.punctuation and prevtup[0] != "":
                    text += " "
                text += tup[0]
                prevtup = (text, tup[1])
            else:
                if prevtup[1] == "O" or prevtup[0] not in dictText:
                    if prevtup[0] != "":
                        satz += str(prevtup[0])
                else:
                    if dictText[prevtup[0]] == prevtup[0]:
                        satz += str("[[" + prevtup[0] + "]]")
                    else:
                        satz += str("[[" + dictText[prevtup[0]] + "|" + prevtup[0] + "]]")
                if tup[0] not in string.punctuation and prevtup[0] != "":
                    satz += str(" ")
                prevtup = (tup[0], tup[1])

        if prevtup[0] != "":
            if tup[0] in dictText:
                satz += str("[[" + dictText[prevtup[0]] + "|" + prevtup[0] + "]]")
            else:
                satz += str(prevtup[0])

        outputList.append(satz)

    return outputList


#Starts here
linkstatistikfilename = "Linkstatistik.txt"
if len(sys.argv) > 1:
    linkstatistikfilename = sys.argv[1]

if len(sys.argv) > 2:
    with open(sys.argv[2], encoding="utf-8") as swfile:
        searchlines = swfile.readlines()
        outputList = analyseSentenses(searchlines, linkstatistikfilename)
        with outputfile_open() as outfile:
            for i in outputList:
                outfile.write(i + "\n")
else:
    eingabe = ""
    while eingabe != " ":
        eingabe = input("Enter sentence, or 'Space' for quit: ")
        if eingabe != " ":
            print(analyseSentenses([eingabe], linkstatistikfilename)[0])

