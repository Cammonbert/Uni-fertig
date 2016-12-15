#########################
# Zoo Simluation 		#
#########################

# IMPORTANT!! Please submit THIS file, a file called animals.py
# and a PDF containing your UML class diagrams!

# We will provide some more help on this exercise in our
# Thursday session!



'''
### Requirements ###

Write a module called 'animals.py', in which you put all the animal
classes. In this exercise, it is essential that you do not write
code that provides the same functionality (e.g. print "Animal" on
the console) twice! Check the log files provided to see what your
program should be able to do.

The descriptions of an animal should be generated based on the class
from which the object was created. There should be one general class
which does the main work, e.g. reading in the images, printing out
the images etc.

IMPORTANT: You can either execute this file with idle,
or execute it like this:

python3 -i zoo.py

(This executes this file and then enters interactive mode, so you
can visit your animals.)

Correct implementation of the above functionality with a good
class design: worth 4 points.

Draw a UML class diagram for your application (worth 3 points).


'''

from animals import *

IMG_PATH = "ascii-art/"

zoo_img = None
zoo_animals = []

def display_zoo():
    for line in zoo_img:
        print(line)
    print("Animals:")
    for animal in zoo_animals:
        # Hint: the __str__ method of animal
        # will be called from here.
        print("*", animal)
    

if __name__ == "__main__":
    # Read in zoo picture
    zoo_img = read_image(IMG_PATH + "zoo.txt")
        
    # Create the zoo animals
    bear = Mammal("bear", IMG_PATH + "bear.txt")
    zoo_animals.append(bear)
    beaver = Rodent("beaver", IMG_PATH + "beaver.txt")
    zoo_animals.append(beaver)
    cockatoo = LandBird("cockatoo", IMG_PATH + "cockatoo.txt")
    zoo_animals.append(cockatoo)
    duck = WaterBird("duck", IMG_PATH + "duck.txt")
    zoo_animals.append(duck)
    elephant = Mammal("elephant", IMG_PATH + "elephant.txt")
    zoo_animals.append(elephant)
    fish = Fish("fish", IMG_PATH + "fish.txt")
    zoo_animals.append(fish)
    gorilla = Mammal("gorilla", IMG_PATH + "gorilla.txt")
    zoo_animals.append(gorilla)
    rabbit = Rodent("rabbit", IMG_PATH + "rabbit.txt")
    zoo_animals.append(rabbit)
    stork = WaterBird("stork", IMG_PATH + "stork.txt")
    zoo_animals.append(stork)
    vulture = LandBird("vulture", IMG_PATH + "vulture.txt")
    zoo_animals.append(vulture)

    # Start zoo simulation
    display_zoo()

    '''
    In the interactive mode, you can now visit the animals
    of your zoo by typing for instance
    duck.visit()
    duck.swim()
    display_zoo()
    beaver.visit()
    ...
    '''
