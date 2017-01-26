dictionary = dict()
with open("Linktext.txt", encoding="utf-8") as readfile:
    for i in readfile:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
with open("Over200.txt", "a", encoding="utf-8") as writefile:
    for i in sorted(dictionary):
        if dictionary[i] >= 200:
            writefile.write(str(dictionary[i]) + " , " + i)