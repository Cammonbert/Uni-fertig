dictionary = dict()
with open("data/Linktext.txt", encoding="utf-8") as readfile:
    for i in readfile:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
with open("data/Linkstatistik.txt","w",encoding="utf-8") as writefile:
    for i in sorted(dictionary):
        writefile.write(str(dictionary[i]) + "\t" + i)
