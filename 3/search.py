from os import listdir #imports name listdir from module directory os

desiredWord = input ('Type the word you want to look for ')

h = open('hits.txt', 'a') #creates or opens file hits.txt for appending
total = 0 #variable containing number of hits

for t in listdir("texts"): #for loop through the names of files in directory "texts"
    file = open("texts/"+t) # opens found file(variable "t" contains its name)
                            # from directory "texts" for reading
    contents = file.readlines() # readlines liest die zeilen in die liste contents rein

    for line in contents: # for loop though the text lines of the opened file
        if desiredWord in line: #tests if line contains desired word
            total += 1 #increments number of hits
            print (t) #prints out the name of the file containing the desired word
            print (line) #prints out the line of text containing the desired word

    file.close()



h.write(desiredWord + " " + str(total) + '\n') # writes the desired word and the number of hits
                                           # converted into a stringto the file 'hits.txt'

h.close()