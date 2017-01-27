import re


def stringsucheinter():
    reg = r"(\d+)([ , ]{3})(.+)([ ]{8})(.+)"
    list2 = list()
    eingabe = input("String: ")
    while eingabe != " ":
        with open("Over200.txt", encoding="utf-8") as readfile:
            for line in readfile:
                list1 = re.findall(reg, line)
                for item in list1:
                    if eingabe == item[4]:
                        list2.append((item[2], int(item[0])))
        if list2:
            print(sorted(list2, key=lambda x: x[1], reverse=True)[0][0])
        list2.clear()
        eingabe = input("string: ")


def stringsuchetext(datei):
    reg = r"(\d+)([ , ]{3})(.+)([ ]{8})(.+)"
    list2 = list()
    writefile = open("Stringsucheergebnis.txt", "w", encoding="Utf-8")
    writefile.truncate()
    writefile.close()
    writefile = open("Stringsucheergebnis.txt", "a", encoding="Utf-8")
    eingabedatei = open(datei, "r", encoding="Utf-8")
    for x in eingabedatei.readlines():
        eingabe = x
        with open("Over200.txt", encoding="utf-8") as readfile:
            for line in readfile:
                list1 = re.findall(reg, line)
                for item in list1:
                    if eingabe == item[4] + "\n":
                        list2.append((item[2], int(item[0])))
        if list2:
            writefile.write(sorted(list2, key=lambda x: x[1], reverse=True)[0][0] + "\n")
        list2.clear()


stringsuchetext("names_line_by_line.txt")