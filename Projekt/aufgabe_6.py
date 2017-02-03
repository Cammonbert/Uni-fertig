from nltk.tag import StanfordNERTagger
import sys

import aufgabe_4
import aufgabe_5b

def analyseSentenses(inputText, linkstatistikfilename, tffilename, idffilename):
    jar = 'stanford-ner-2016-10-31/stanford-ner.jar'
    model = 'stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz'
    st = StanfordNERTagger(model, jar)

    searchwords = aufgabe_4.createSearchWordDic(inputText, st)

    for val in searchwords:
        searchwords[val] = {}

    #create ranking
    with open(linkstatistikfilename, encoding="utf-8") as readfile:
        for i in readfile:
            tuple = i.rstrip().split("\t")
            if len(tuple) > 2:
                if tuple[2] in searchwords:
                    if len(searchwords[tuple[2]]) < 3:
                        searchwords[tuple[2]][tuple[1]] = int(tuple[0])
                    else:
                        minKey = min(searchwords[tuple[2]], key=searchwords[tuple[2]].get)
                        minVal = searchwords[tuple[2]][minKey]
                        if int(tuple[0]) > minVal:
                            searchwords[tuple[2]].pop(minKey)
                            searchwords[tuple[2]][tuple[1]] = int(tuple[0])

    dictIdf = aufgabe_5b.getIdf(idffilename)
    dictTf = aufgabe_5b.getTf(tffilename)
    dictDocRanking = aufgabe_5b.getRatingList(dictTf, dictIdf, inputText)
    dictText = dict()

    for sWord in searchwords:
        docList = []
        for doc in searchwords[sWord]:
            docList.append(doc)
        Ranc = 0.0
        for element in reversed(docList):
            if dictDocRanking.get(element, 0.0) >= Ranc:
                Ranc = dictDocRanking.get(element, 0.0)
                dictText[sWord] = element

    return aufgabe_4.createOutList(inputText, dictText, st)



#Starts here
if __name__ == "__main__":
    linkstatistikfilename = "data/Linkstatistik.txt"
    if len(sys.argv) > 1:
        linkstatistikfilename = sys.argv[1]

    tffilename = "data/tf.csv"
    if len(sys.argv) > 2:
        tffilename = sys.argv[2]

    idffilename = "data/idf.csv"
    if len(sys.argv) > 3:
        idffilename = sys.argv[3]

    if len(sys.argv) > 4:
        with open(sys.argv[4], encoding="utf-8") as swfile:
            searchlines = swfile.read()
            outputList = analyseSentenses(searchlines, linkstatistikfilename, tffilename, idffilename)
            with aufgabe_4.outputfile_open() as outfile:
                for i in outputList:
                    outfile.write(i + "\n")
    else:
        eingabe = input("Enter sentence: ")
        if eingabe != "":
            print(analyseSentenses(eingabe, linkstatistikfilename, tffilename, idffilename)[0])