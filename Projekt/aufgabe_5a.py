import string
import csv
import math
from nltk.stem.porter import PorterStemmer
from collections import defaultdict


def safeStemmer(word):
    # PortStemmer seems to crash on some words, i.e. 'aed', 'aing', 'aeds'
    # this is a workaround
    try:
        return PorterStemmer().stem(word)
    except IndexError:
        return word

#Starting point

dictTokenFreq = dict()
dictDocTokenFreq = defaultdict(dict)

with open("data/Linkstatistik.txt", encoding="utf-8") as readfile:
    for i in readfile:
        tuple = i.rstrip().split("\t")
        if len(tuple) > 2:
            linktext = tuple[2].lower()
            linktext = linktext.translate(str.maketrans('', '', str(string.punctuation + '(' + ')')))

            for word in linktext.rstrip().split(" "):
                word = safeStemmer(word)
                dictTokenFreq[word] = dictTokenFreq.get(word, 0) + int(tuple[0])
                dictDocTokenFreq[tuple[1]][word] = int(dictDocTokenFreq[tuple[1]].get(word, 0) + int(tuple[0]))

    with open('data/idf.csv', 'w', encoding="utf-8") as csvfile:
        idfWriter = csv.writer(csvfile)
        for token in dictTokenFreq:
            idfWriter.writerow([token, math.log(len(dictDocTokenFreq) / dictTokenFreq[token])])

    with open('data/tf.csv', 'w', encoding="utf-8") as csvfile:
        tfWriter = csv.writer(csvfile)
        for document in dictDocTokenFreq:
            maxVal = max(dictDocTokenFreq[document].values())
            writeLine = [document]

            for token in dictDocTokenFreq[document]:
                writeLine.append(token)
                writeLine.append(float(dictDocTokenFreq[document][token] / maxVal))

            tfWriter.writerow(writeLine)
