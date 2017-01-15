def read_links():
    with open("Linktext.txt","a",encoding="utf-8") as writefile:
        with open("wikilinks_en.txt",encoding="utf-8") as readfile:
            for line in readfile:
                if "|" in line:
                    line = line.replace("[","",2)
                    line = line.replace("|","        ",1)
                    line = line.replace("]","",2)
                    writefile.write(line)

read_links()
