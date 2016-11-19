from nltk.corpus import brown

brown_words = brown.words()  # Speichern brown corpus in eine Liste
words = []  # Erstellen eine Liste

for word in brown_words:
    if len(word) >= 5:  # Alle Wörter, die mehr als 5 Buchstaben haben, werden in der Liste 'words' gespeichert
        words.append(word)

def top_suffix(words, sufLen): #Erstellen Funktion top_suffix
    suffixes = {}  # Erstellen ein leeres Dictionary für die Suffixes

    # Aus allen Wörtern das Suffix extrahieren.
    # Suffix zählen, in dem es im Dictionary suffixes gespeichert wird
    for word in words:  # geht durch jedes Wort
        suffix = word[-sufLen:]  # Suffix aus Wort extrahieren: die letzten sufLen Zeichen sind das Suffixx.
        if suffix in suffixes:  # Prüfen, ob Suffix schon vorhanden.
            suffixes[suffix] += 1  # wenn findet, fügt in die Liste Suffixes hinzu:
        else:
            suffixes[suffix] = 1  # wenn nicht, return 1

    top_ten_suffixes = {}  # Leeres dict für die ersten zehn Suffixe erstellen

    for topsuffix in sorted(suffixes, key=suffixes.get)[-10:]:  # Sortieren der Suffixes nach Value und Verwenden der zehn häufigsten
        top_ten_suffixes[topsuffix] = suffixes[topsuffix]  # Befüllen des Dictionarys mit den top ten Keys und entsprechenden Values.

    return top_ten_suffixes


# Sanity Tests
TopSuffixes = top_suffix(words, 2)
print(TopSuffixes)
TopSuffixes = top_suffix(words, 3)
print(TopSuffixes)
