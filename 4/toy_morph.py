from nltk . corpus import brown # imports corpus brown from nltk

def top_suffixes (words, sufLen): # defines funktion that finds the mist common suffix
    dictionary = {} # make an empty dictionary with common suffixes
    for word in words: # for loop through all words in the corpus
        if len(word) >= 5  and len(word) >= sufLen: # tests if the word is longer than 5 letters and longer than the
            # length of the suffix (in case we want to search for suffixes longer than 2 or 3 letters)
            suffix = word[-sufLen:] # suffix is defined as the part of word in the end of it of the set length
            if suffix in dictionary: # tests if we already have this suffix in the dictionary
                dictionary[suffix] += 1 # if yes, increments the quantity of the suffix
            else:
                dictionary[suffix] = 1 # if not, adds new suffix in the list

    topTenDictionary = {} # creates empty dictionary to be filled with 10 most common suffixes
    topTenList = sorted(dictionary, key = dictionary.get)[-10:] # sorts the contents of dictionary by value.
    # uses get() function to get the values of the dictionary, key=  takes the returned value of the fkt dictionary.get
    # to compare the elements of the dictionary

    for listElement in topTenList: # for loop throuth the elements of the list with 10 common suffixes
        topTenDictionary[listElement] = dictionary[listElement] # under the key listElement saves the values from the
        # old dictionary to the new dictionary

    return topTenDictionary # returns the dictionary with 10 most common suffixes

def top_prefixes (words, prefLen): #analog to top_suffixes
    dictionary = {}
    for word in words:
        if len(word) >= 5 and len(word) >= prefLen:
            prefix = word[:prefLen]
            if prefix in dictionary:
                dictionary[prefix] += 1
            else:
                dictionary[prefix] = 1

    topTenDictionary = {}
    topTenList = sorted(dictionary, key = dictionary.get)[-10:]

    for listElement in topTenList:
        topTenDictionary[listElement] = dictionary[listElement]

    return topTenDictionary

def longest_word (words, prefLen): # function to find the longest word with the most common prefix
    dictionary = top_prefixes(words, prefLen) # creates a dictionary with the common prefixes (call the function)
    topPrefix = sorted(dictionary, key = dictionary.get)[-1] # one most common suffix
    longword = [''] # empty list
    print(topPrefix) # just to make it more clear and nice
    for word in words: # for loop through the elements of the corpus
        if word[:prefLen] == topPrefix :      # tests if the prefix of the word is one of the most common prefixes
            if len(word) > len(longword[0]) : # tests if the word from the corpus is longer than the word that we
                                              # already have in the list
                longword = [word] # if yes, overwrites with the new longer word
            elif len(word) == len(longword[0]) : # if the new and the word that we already have are of the same length
                if word not in longword :        # and thw word is not alredy in the list
                    longword += [word]           # add the new word to the list

    return longword

def shortest_word (words, sufLen): # analog to longest_word()
    dictionary = top_suffixes(words, sufLen)
    topSuffix = sorted(dictionary, key = dictionary.get)[-1]
    shortword = ['']
    print(topSuffix)
    for word in words:
        if word[-sufLen:] == topSuffix :
            if len(shortword[0]) == 0 or len(word) < len(shortword[0]) : # tests if there is no elements in the list of
                                                                         # the shortest word yet the new word is shorter
                                                                         # than the word that we already have in the list
                shortword = [word]
            elif len(word) == len(shortword[0]) :
                if word not in shortword :
                    shortword += [word]

    return shortword

brown_words = brown.words()

print (top_suffixes(brown_words, 2))
print (top_suffixes(brown_words, 3))
print (top_prefixes(brown_words, 3))
print (top_prefixes(brown_words, 2))

file = open('tokens.txt', 'w') # opens file for writing

file.write (str(top_suffixes(brown_words, 2)) + '\n')
file.write (str(top_suffixes(brown_words, 3)) + '\n')
file.write (str(top_prefixes(brown_words, 3)) + '\n')
file.write (str(top_prefixes(brown_words, 2)) + '\n')

file.close()

print (longest_word(brown_words, 1)) #1-6 just to test different variants
print (longest_word(brown_words, 2))
print (longest_word(brown_words, 3))
print (longest_word(brown_words, 4))
print (longest_word(brown_words, 5))
print (longest_word(brown_words, 6))

print (shortest_word(brown_words, 1))
print (shortest_word(brown_words, 2))
print (shortest_word(brown_words, 3))
print (shortest_word(brown_words, 4))
print (shortest_word(brown_words, 5))
print (shortest_word(brown_words, 6))
