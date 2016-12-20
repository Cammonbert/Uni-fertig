from nltk.book import *

print(len(sorted((set([w.lower() for w in text1])))))# Length = 17231

print(len(sorted(([w.lower() for w in set(text1)]))))# Length = 19317

# Die Unterschied ist die Menge die beide Zeilen zurückliefern.
# 2. hat noch die Duplikate, denn die Menge behält z.B."am" und "Am", "dem" und "Dem" usw.