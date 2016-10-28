pronouns = open("en_pronouns.txt").read().split(" ") #opens file and splits it by spaces
stopWords = open("en_stopwords.txt").read().split(" ") #opens file and splits it by spaces

mySetPron = set(pronouns) #fills the contents of the list of pronouns into the set
mySetStop = set(stopWords) #fills the contents of the list of stopwords into the set

#1. Prints the number of pronouns included in the list of stopwords.
print ("There are",len(mySetPron.intersection(mySetStop)), "pronouns in the list of stopwords.")

#2. Prints the number of elements in the set of stopwords without the ones included in the set of pronouns.
print ("There are",len((mySetStop)-(mySetPron)),"stopwords without the ones included in the set of pronouns.")

#3. Prints the boolean values True or False, based on the test if the list of stopwords includes
# all elements in the list of pronouns.
print ("The statement that the list of stopwords includes all elements in the list of pronouns is: ",
       (mySetPron)==(mySetPron.intersection(mySetStop)))

#4. Prints the number of elements that are contained in the list of pronouns but not in the list of stopwords.
print ("The list of pronouns contains",len((mySetPron)-mySetPron.intersection(mySetStop)),
       "elements that are not included in the list of stopwords.")