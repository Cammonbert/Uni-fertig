with open("Linktext.txt", "w", encoding="utf-8") as writefile:
    with open("wikilinks_en.txt", encoding="utf-8") as readfile:
        foundLinkBeg = False
        hasText = False
        linkText = ""
        textText = ""
        prevChar = ""

        for line in readfile:
            for ch in line:
                if ch == "\n":
                    break

                if prevChar == "[" and ch == "[":
                    foundLinkBeg = True
                    hasText = False
                    linkText = ""
                    textText = ""
                    continue
                if prevChar == "]":
                    if ch == "]":
                        if foundLinkBeg is True:
                            if hasText is True and textText != "":
                                writefile.write(linkText + "\t" + textText + "\n")
                            else:
                                writefile.write(linkText + "\t" + linkText + "\n")
                        foundLinkBeg = False
                        hasText = False
                    else:
                        if hasText is True:
                            textText += "]"
                        else:
                            linkText += "]"
                    continue

                prevChar = ch

                if ch == "]":
                    continue

                if foundLinkBeg is True:
                    if ch == "|":
                        hasText = True
                        continue
                    if hasText is True:
                        textText += ch
                        continue
                    if linkText == "":
                        if ch == "#" or ch == "/":
                            foundLinkBeg = False
                            hasText = False
                    linkText += ch

            if hasText is False:
                foundLinkBeg = False
                linkText = ""
                textText = ""
                prevChar = ""
            else:
                textText += " "
                prevChar = " "

    writefile.write("\n")
