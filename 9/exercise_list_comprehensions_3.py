######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# List Comprehensions                #
######################################

# Exercise 3


''' (2 Points)

Rewrite the function f1 in function f2 using a single
list comprehension.

'''

def f1(words):
    result = []
    for word in words:
        wordlenpair = (word, len(word))
        result.append(wordlenpair)
    return result

def f2(words):
    '''
    >>> f2(['Python', 'is', 'great'])
    [('Python', 6), ('is', 2), ('great', 5)]
    '''
    return [(word, len(word)) for word in words]


# This automatically tests your code
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
