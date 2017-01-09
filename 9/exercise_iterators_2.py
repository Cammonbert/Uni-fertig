######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# Iteratoren                         #
######################################

'''
EXERCISE 2:

As we have seen in the lecture, len() cannot be applied to iterators, as
they return one value at a time, not knowing how many will follow. This is
actually an advantage when working with large data files, as it saves
memory (the file can be loaded in to memory just line by line, not all
at once).

However, we cannot ask Python for the length of an iterator (try out the
following counter-example using the shell):

    myIter = iter([1, 2, 3]) # creating an iterator for the sequence (list)

    len(myIter) # will give you an error

The following function computes the average of a sequence of numbers:

    def avg(sequence):
        return sum(sequence) / len(sequence)

It doesn't work for iterators.

Reimplement the avg function so that it can be applied to iterators.

(3 points)

'''


def avg(iterable):
    no = 0
    on = 0
    for n in iterable:
        on += 1
        no += n
    return no/on


# Testing

myIter = iter([0,100])
print(avg(myIter))