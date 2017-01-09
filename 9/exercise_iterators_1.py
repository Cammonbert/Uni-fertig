######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# Iteratoren                         #
######################################

'''
EXERCISE 1

Reimplement the builtin "enumerate." Each call of the "next" method
should return a pair (tuple) containing the count (starting from 0) and the value
obtained from iterating over the sequence the function is applied to. To keep
things simple, you can assume that "enumerate" is applied to an ordered sequence type 
such as a list or string.

(3 points)

Bonus: You can earn one additional point if your code also works with unordered 
collection types such as sets or dictionaries.

(1 point)
'''

class myEnumerate:
    def __init__(self, iterable):
        self.liste = iterable
        self.index = -1
        self.count = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        self.index += 1
        if self.index >= len(self.liste):
            raise StopIteration
        return self.count, self.liste[self.index]

for (i, ch) in myEnumerate("Python"):
    print(i, ch)

# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n