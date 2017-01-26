import re, math
from collections import Counter

WORD = re.compile(r'\w+')
cosines = dict()

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text = input("Enter query, or just hit ENTER to quit.")


vector = text_to_vector(text)
with open("donald100.txt", encoding="utf") as readfile:
    for line in readfile:
       cosine = get_cosine(text_to_vector(line), vector)
       if(cosine > 0):
        cosines[cosine] = line


#for i in reversed(sorted(cosines.keys())):
#        print(i, ':' , cosines[i])


first2pairs = {k: cosines[k] for k in sorted(cosines.keys(),reverse=True)[:3]}
print(first2pairs)