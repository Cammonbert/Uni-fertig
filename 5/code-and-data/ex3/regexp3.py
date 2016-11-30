''' 3. Extracting noun phrases (4 Points)

The file "wsj00-pos-oneline.txt" contains a sample of POS tagged text. Implement a program that reads this file and prints
all noun phrases that occur in the text. To keep things simple, take noun
phrases to be the following sequence of parts of speech:

    DT + zero or more JJ + NN

where DT is the POS for determiners like "the" or "a", JJ is the POS for
adjectives, and NN is the pos for nouns.

Example:

python3 regexp3.py wsj00-pos-oneline.txt

should ** print **:

the/DT board/NN
a/DT nonexecutive/JJ director/NN
the/DT Dutch/NN
a/DT nonexecutive/JJ director/NN
this/DT British/JJ industrial/JJ conglomerate/NN
...

'''

import sys
import re

def main():

    with open(sys.argv[1]) as f:
        text = f.read()
        regex = r"([\w]+/DT)\s+([\w]+/JJ\s+)*([\w]+/NN)"
        pattern = re.compile(regex, re.IGNORECASE)
        for m in re.finditer(pattern, text):
            print(m.group())
    f.close()

    return

if __name__ == '__main__':
    main()
