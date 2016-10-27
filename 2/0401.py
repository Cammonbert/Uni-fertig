line = open('numbers.txt').read() # reads the file contents into the variable line

A = line.split(' ') # uses the split string operation to create a list
B = [int(A[3])] # uses the built-in function int() to convert A[3] to an integer  
B.append(round(float(A[4]))) # converts the 5th(because we start to count with 0) element of the
 # list A into a float number, rounds it to the whole number and adds to the list B.

print(line) #prints the contents of the file numbers.txt as a string

#Aufg.2.2
print(B)

#Aufg.2.3
print (len(B))

#Aufg.2.4
print (int(B[0]+B[1]))