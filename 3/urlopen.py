from urllib.request import urlopen # imports name 'urlopen' from module urllib
from string import ascii_lowercase # imports name 'ascii_lowercase' containing letters from a to z from module 'string'

totalaz = 0  # variable containing the number of founded word definitions in the whole dictionary from a to z

for letter in ascii_lowercase : # for loop that allows us to search thorough the letters from a to z
                                # in the url of the page

   totaleach = 0 # variable containing the number of founded word definitions for each letter in the dictionary

   for line in urlopen('http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_' + letter + '.html'):
                # for loop through the pages of the online dictionary,
                # variable letter goes through the letters from a to z
       if line.decode("utf-8", 'ignore').startswith('<P><B>'): # tests if the line in html begins with <P><B>
                                                               # (we looked it up in the source code of the page)
                      # urlopen returns the result as bytearray, we decode it with .decode("utf-8") to string
                      # with 'ignore' parameter we ignore the errors, so that program doesn't stop without giving a result

           totaleach += 1 # goes through each line and counts the number of found definitions

   print ('In dem Wörterbuch gibt es '+ str(totaleach) + ' Wörter die mit der Buchstabe ' + letter.upper() + ' anfangen.')
                      # prints the result on the console,
                      # number of found definitions converted into string with the help of str(total)
                      # letter.upper() to print out letters in upper case for better readability
   totalaz += totaleach

print ('\nInsgesamt gibt es ' + str(totalaz) + ' Wörter in dem Wörterbuch')