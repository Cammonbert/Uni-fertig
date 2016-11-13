from os import listdir
#print(listdir("texts"))

h=open('hits.txt', 'w')


countComputational=0
countLinguistics=0
countProcessing=0
countChunking=0
countCoreference=0
countHtml=0
countMachine=0

for t  in listdir("texts"):
    file = open("texts/"+t)
    contents = file.readlines() #readlines liest die zeilen in die liste contents rein

    for line in contents:
        if "computational" in line:
            countComputational+=1;
            print (t)
            print (line)

        if "linguistics" in line:
            countLinguistics+=1
            print(t)
            print(line)

        if "processing" in line:
            countProcessing += 1
            print(t)
            print(line)

        if "chunking" in line:
            countChunking += 1
            print(t)
            print(line)

        if "coreference" in line:
            countCoreference += 1
            print(t)
            print(line)

        if "html" in line:
            countHtml += 1
            print(t)
            print(line)

        if "machine" in line:
            countMachine += 1
            print(t)
            print(line)

h.write('computational '+ str(countComputational)+'\n')
h.write('linguistics '+ str(countLinguistics) +'\n')
h.write('processing '+ str(countProcessing) +'\n')
h.write('chunking '+ str(countChunking) +'\n')
h.write('coreference '+ str(countCoreference) +'\n')
h.write('html '+ str(countHtml) +'\n')
h.write('machine '+ str(countMachine) +'\n')

