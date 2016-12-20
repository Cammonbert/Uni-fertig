import random
from nltk.book import *

class Analyzer:

    def __init__(self, text):
        self.text = text
        self.freqdist = FreqDist(text)
        self.hapax = []
        self.lexicon = sorted(set(self.text))
        self.anzahlTokens = len(self.text)
        self.anzahlLexicon = len(self.lexicon)
        self.maxlen = 0
        self.letters = 0
        self.infreqwords = []
        self.printStats()

    #Anzahl der Tokens
    def numberOfTokens(self):
        return self.anzahlTokens

    #Liste der Types
    def vocabulary(self):
        return self.lexicon

    #Anzahl der Types
    def vocabularySize(self):
        return self.anzahlLexicon

    #Die lexikalische Vielfalt des Textes
    def lexicalDiversity(self):
        self.diversity = (self.anzahlTokens) / (self.anzahlLexicon)
        return self.diversity

    #Das längste Wort und falls es mehrere solche Wörter gibt, gibt zufälliges Wort zurück
    def longestWord(self):
        self.maxlen = max(len(word) for word in self.text)
        self.longestword = random.choice([word for word in self.text if len(word) == self.maxlen])
        return self.longestword

    #Häufigkeit des längsten Wortes
    def longestWordFD(self):
        self.freqLword = self.freqdist[self.longestword]
        return self.freqLword

    #Das kürzeste Wort und falls es mehrere solche Wörter gibt, gibt zufälliges Wort zurück
    def shortestWord(self):
        self.minlen = min(len(word) for word in self.text)
        self.sword = random.choice([word for word in self.text if len(word) == self.minlen])
        return self.sword

    #Häufigkeit des kürzesten Wortes
    def shortestWordFD(self):
        self.freqSword = self.freqdist[self.sword]
        return self.freqSword

    #Liste von Wörter, die nur einmal im Text vorkommen
    def hapaxes(self):
        self.hapax = self.freqdist.hapaxes()
        return self.hapax

    #Anzahl von Wörter, die nur einmal im Text vorkommen
    def numberOfHapaxes(self):
        self.numhapax = len(self.hapax)
        return self.numhapax

    #Liste der selten benutzte Wörter, die doppelt so groß ist wie die Liste der Hapaxes
    def infrequentWords(self):
        self.listInfreqW = []
        for key in (key for key in sorted(self.freqdist, key=self.freqdist.get) if self.freqdist[key] > 1):
            self.listInfreqW.append(key + " (" + str(self.freqdist[key]) + ")")
        return self.listInfreqW[:2 * self.numhapax]

    #Set von selten benutzten Wörter, die keine Hapaxes sind
    def infrequentWordsNotHapaxes(self):
        self.infreqwordsnotHapaxes = set(w for w in self.lexicon if self.freqdist[w] < 10 and self.freqdist[w] > 1)
        return self.infreqwordsnotHapaxes

    #Durchschnittliche Länge der Wörter  des Textes
    def avWordLength(self):
        for elem in self.text:
            self.letters += len(elem)
        self.word_average = self.letters / self.anzahlTokens
        return self.word_average

    #Information über den Objekt
    def printStats(self):
        print("Number of tokens:", str(self.numberOfTokens()))
        print("Vocabulary:", str(self.vocabulary()))
        print("Size of the vocabulary:", str(self.vocabularySize()))
        print("Diversity:", str(self.lexicalDiversity()))
        print("The longest word:", str(self.longestWord()))
        print("The longest word frequency:", str(self.longestWordFD()))
        print("The shortest word:", str(self.shortestWord()))
        print("The shortest word frequency:", str(self.shortestWordFD()))
        print("Hapaxes:", str(self.hapaxes()))
        print("The number of hapaxes in the text:", str(self.numberOfHapaxes()))
        print("Infrequent words:", str(self.infrequentWords()))
        print("Infrequent words not hapaxes:", str(self.infrequentWordsNotHapaxes()))
        print("The average word length:", str(self.avWordLength()))
        print("Frequ. Dist:", str(self.freqdist))


test=Analyzer(text1)