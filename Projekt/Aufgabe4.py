from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import re


jar = 'C:/Users/Adri/stanford-ner-2016-10-31/stanford-ner.jar'
model = 'C:/Users/Adri/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz'


def interactive():
    reg = r"(\d+)([ , ]{3})(.+)([ ]{8})(.+)"
    list2 = list()
    st = StanfordNERTagger(model, jar)
    sentence = input("Enter sentence, or Leer for quit.")
    satz = ""
    while sentence != " ":
        sentence = word_tokenize(sentence)
        print(st.tag(sentence))
        tags = st.tag(sentence)
        for tup in tags:
            if tup[1] == "O":
                satz += str((tup[0] + " "))
            else:
                with open("Over200.txt", encoding="utf-8") as readfile:
                    for line in readfile:
                        list1 = re.findall(reg, line)
                        for item in list1:
                            if tup[0] == item[4]:
                                list2.append((item[2], int(item[0])))
                if list2:
                    satz += str("[[" + (sorted(list2, key=lambda x: x[1], reverse=True)[0][0] + "|" + tup[0] + "]] "))
                    list2.clear()
                else:
                    satz += str((tup[0] + " "))
        print(satz)
        satz = ""
        sentence = input("Enter sentence, or Leer for quit.")


def noninteractive(datei):
    reg = r"(\d+)([ , ]{3})(.+)([ ]{8})(.+)"        #regex erstellen
    list2 = list()                                  #liste erstellen
    st = StanfordNERTagger(model, jar)              #stanfordtagger bestimmen
    #Aufgabe4_noninteractive.txt leeren
    writefile = open("Aufgabe4_noninteractive.txt", "w")
    writefile.truncate()
    writefile.close()

    writefile = open("Aufgabe4_noninteractive.txt", "w")    #öffne writefile
    eingabedatei = open(datei, "r")                         #öffne eingabedatei
    for thing in eingabedatei.readlines():                  #für jede line in eingabedatei
        satz = word_tokenize(thing)                         #line tokenizen
        tags = st.tag(satz)                                 #tags liste erstellen
        writefile.write("\n\n" + str(thing) + "\n")          #tags liste in datei schreiben
        for tup in tags:                                    #für jedes tupel in der liste tags
            if tup[1] == "O":                               #wenn value O ist
                writefile.write(str((tup[0] + " ")))        #schreibe key
            else:                                           #ansonsten
                with open("Over200.txt", encoding="utf-8") as readfile:         #öffne Over200.txt
                    for line in readfile:                                       #für jede line darin
                        list1 = re.findall(reg, line)                           #regexe finden
                        for item in list1:                                      #für jedes item in liste aus regexen
                            if tup[0] == item[4]:                               #wenn key = eingabetext
                                list2.append((item[2], int(item[0])))           #liste 2 erstellen mit anzahl und wikiartikel
                if list2:                                                       #wenn etwas in liste2 steht
                    #ersten(und damit höchsten) key mit artikelname in writefile schreiben
                    writefile.write(str("[[" + (sorted(list2, key=lambda x: x[1], reverse=True)[0][0] + "|" + tup[0] + "]] ")))
                    list2.clear()                                               #liste2 leeren
                else:                                                           #sonst
                    writefile.write(str((tup[0] + " ")))                        #key einfach schreiben


noninteractive("names_line_by_line.txt")
