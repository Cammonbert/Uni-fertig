import re


def vergleich(x):
    i = 0
    for c in x:
        if c > i:
            i = c
    return i


def stringsuche():
    reg = r"(\d+)([ , ]{3})(.+)([ ]{8})(.+)"
    list2 = list()
    eingabe = input("String: ")
    while eingabe != " ":
        with open("Over200.txt", encoding="utf-8") as readfile:
            for line in readfile:
                list1 = re.findall(reg, line)
                for item in list1:
                    if eingabe == item[4]:
                        list2.append(int(item[0]))
        x = str(vergleich(list2))
        with open("Over200.txt", encoding="utf-8") as readfile:
            for line in readfile:
                list1 = re.findall(reg, line)
                for item in list1:
                    if eingabe == item[4]:
                        if x == item[0]:
                            man = item[2]
                            print(man)
        eingabe = input("string: ")


stringsuche()
