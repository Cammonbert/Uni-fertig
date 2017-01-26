from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
sentence = input("Enter sentence, or just hit ENTER to quit.")
text = word_tokenize(sentence)
for word in text:
    print(st.tag(word))

