''' 2. POS-Tagged text (4 Points)

The file regexp2_example.txt contains a small sample of
POS-tagged text, where words are represented as follows:

    <W TYPE="part of speech" ...>word</W>

Write a function that reads the file and ** returns ** a list of word-POS 
pairs (see example below).

Example:

read_file("regexp2_example.txt")

should return:

[('FACTSHEET', 'NN1'), ('WHAT', 'DTQ'), ('IS', 'VBZ'), ...]
'''

import sys
import re

def read_file(filename):
    matches = []

    with open(filename) as f:
        text = f.read()
        regex = \
          r"<W\s+TYPE=\"([\w-]*)\"\s+TEIFORM=\"w\">\s*([\w'\s]*[\w'])\s*</W>"
        # compiles regex for using
        pattern = re.compile(regex, re.IGNORECASE)
        # finditer returns the list of found iterators
        for m in re.finditer(pattern, text):
            matches.append((m.group(2),m.group(1)))
    f.close()

    return matches # the resulting list; DO NOT PRINT

def main():
    # for testing
    for (word, pos) in read_file(sys.argv[1]):
        print(word, pos)

if __name__ == '__main__':
    main()
