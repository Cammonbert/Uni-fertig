Dict = {} # create an empty dictionary

for line in open('dictBase.txt'): # for every line in the file
    tmp = line.split("--") # split the line into the list tmp
    Dict[tmp[0]] = tmp[1] # add a pair to the dictionary by using the first element of tmp as the key and the second as its value


#1. Add a statement that prints out the size of the dictionary.
print ("1. There are",len(Dict),"keys in the dictionary.")

#2.  Print out the key-value pair under the key table.
print  ("2. Table is",Dict ["table"])#FRAGE: Wir glauben, dass es die billige Variante sei, wir suchen einfach nur nach Value
# von dem gegebenen Key.
#Wie sucht man aber nach einem Key, sodass die es auch ein Key ausgegeben wird und die passende Value dazu, das verstehen wir nicht.
#oder vielleicht ist es gar nicht möglich?

#3.  Print out each key-value pair separately in a sorted order (hint:  look up the slides).
print ("3.")
for key, val in sorted(Dict.items()):
    print (key, "=>", val) #FRAGE: Warum gibt's new line nach "boat"?

for key in sorted(Dict): #andere Variante
    print(key, "=>", Dict[key])
