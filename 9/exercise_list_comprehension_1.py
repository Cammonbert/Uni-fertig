######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# List Comprehensions                #
######################################

# Exercise 1

''' (3 Points) Write a function called celsiusFahrenheitList1
that creates a list of tuples, where each tuple gives temperatures
in Celsius and Fahrenheit. This function should create one list
for Celsius values from 0 to 100 in steps of 5.
Your function should ONLY use a list expression that comes
after the return statement.
Also, write the function celsiusFahrenheitListConfigurable
using ONLY a list expression. The parameters start, end and stepsize
are all integers, and you may assume that end>start.

Note: Fahrenheit = (( Celsius * 9 ) / 5 ) + 32
'''

def celsiusFahrenheitList():
    '''
    >>> celsiusFahrenheitList()
    [(0, 32.0), (5, 41.0), (10, 50.0), (15, 59.0), (20, 68.0), (25, 77.0), (30, 86.0), (35, 95.0), (40, 104.0), (45, 113.0), (50, 122.0), (55, 131.0), (60, 140.0), (65, 149.0), (70, 158.0), (75, 167.0), (80, 176.0), (85, 185.0), (90, 194.0), (95, 203.0), (100, 212.0)]
    '''
    return [(x,((x*9)/5)+32) for x in range(0,101,5)]

def celsiusFahrenheitListConfigurable(start, end, stepsize):
    '''
    >>> celsiusFahrenheitListConfigurable(20, 80, 3)
    [(20, 68.0), (23, 73.4), (26, 78.8), (29, 84.2), (32, 89.6), (35, 95.0), (38, 100.4), (41, 105.8), (44, 111.2), (47, 116.6), (50, 122.0), (53, 127.4), (56, 132.8), (59, 138.2), (62, 143.6), (65, 149.0), (68, 154.4), (71, 159.8), (74, 165.2), (77, 170.6), (80, 176.0)]
    >>> celsiusFahrenheitListConfigurable(50, 60, 1)
    [(50, 122.0), (51, 123.8), (52, 125.6), (53, 127.4), (54, 129.2), (55, 131.0), (56, 132.8), (57, 134.6), (58, 136.4), (59, 138.2), (60, 140.0)]
    '''
    return [(x,((x*9)/5)+32) for x in range(start,end+1,stepsize)]

    

# This automatically tests your code
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
