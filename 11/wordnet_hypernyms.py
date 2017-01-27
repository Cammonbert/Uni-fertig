import nltk

# Read in text.
text = None
with open("ada_lovelace.txt") as f:
    text = f.read()

# Split into sentences
sentences = nltk.sent_tokenize(text)

# Split into tokens
tokens = []
for sentence in sentences:
    tokens += nltk.word_tokenize(sentence)



# POS tagging
pos_tags = nltk.pos_tag(tokens)



# lemmatize nouns (any token whose POS tags starts with "N")
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()
noun_lemmas = []
for (token, pos) in pos_tags:
    if pos.startswith("N"):
        noun_lemmas.append(lemmatizer.lemmatize(token, wordnet.NOUN))




# find words that are hyponyms to the following three synsets
relative = wordnet.synsets("relative",pos ='n')[0] # TODO: Synset for the most frequent sense of the noun 'relative'
science = wordnet.synsets("science", pos='n')[0] # TODO: Synset for the most frequent sense of the noun 'science'
illness = wordnet.synsets("illness", pos='n')[0] # TODO: Synset for the most frequent sense of the noun 'illness'




def hypernymOf(synset1, synset2):
    if synset1 == synset2:
        return True
    for hypernym in synset1.hypernyms():
        if synset2 == hypernym:
            return True
        if hypernymOf(hypernym, synset2):
            return True
    return False


#Erstellen Liste mit Synsets
listOfSynsets = [relative, science, illness]

#Für jeden gegebene Synset
for elem in listOfSynsets:
    words = []
    for noun in noun_lemmas:                        #Für jedes Wort in noun_lemmas
        nounhyp = wordnet.synsets(noun, pos='n')    #erstellen Synset
        for i in nounhyp:
            if hypernymOf(i, elem) == True:         # Falls erstellende Synset ist Hypernum vom gegebende Synset
                words.append(noun)                  # fügen das Wort in der Liste
    print("Synset: ",elem.name())                   # Synset Name
    print("Definition: ",elem.definition())         # wordnet gloss (defintion)
    print("Lemmas: ",set(words))                    # Set mit worter die zum Synset gehören
    print("Occurrences: ",len(words))               # Anzahl der Worter in ada_lovelace.txt die zum Synset gehören



