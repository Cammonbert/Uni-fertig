import re


def read_links():
    with open("Linktext.txt","a",encoding="utf-8") as writefile:
        with open("wikilinks_en.txt",encoding="utf-8") as readfile:
            for line in readfile:
                if "|" in line:
                    line = line.replace("[","",2)
                    line = line.replace("|","        ",1)
                    line = line.replace("]","",2)
                    writefile.write(line)
        writefile.write("\n")


def linkstatistik():
    dictionary = dict()
    with open("Linktext.txt", encoding="utf-8") as readfile:
        for i in readfile:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    with open("Linkstatistik.txt","a",encoding="utf-8") as writefile:
        for i in sorted(dictionary):
            writefile.write(str(dictionary[i]) + " , " + i)


def linkstatistikover200():
    dictionary = dict()
    with open("Linktext.txt", encoding="utf-8") as readfile:
        for i in readfile:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    with open("Over200.txt","a",encoding="utf-8") as writefile:
        for i in sorted(dictionary):
            if dictionary[i] >=200:
                writefile.write(str(dictionary[i]) + " , " + i)

def stringsuche():
    reg = r"(\d+)([ , ]{3})(.+)([ ]{8})(.+)"
    eingabe = input("string: ")
    with open("Over200.txt",encoding="utf-8") as readfile:
        for line in readfile:
            list1 = re.findall(reg, line)
            for item in list1:
                if eingabe == item[4]:
                    print(item[2])
stringsuche()
