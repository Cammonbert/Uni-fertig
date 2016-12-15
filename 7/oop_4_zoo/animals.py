#############################
# UTILITIES                 #
#############################

'''
e.g. a function that reads in the images
'''
def read_image(path):
    f=open(path)
    return f

#############################
# ANIMALS                   #
#############################

class Animal:

    def __init__(self,n,p):
        self.name=n
        self.path=p

    def eat(self):
        print("I am a", self.name, "and I am EATING")

    def sleep(self):
        print("I am a", self.name, "and - yawn... ~~~~ ZZZzzzz ~~~~")

    def visit(self):
        pass

    #def __str__(self) und visit() fehlt noch



class Mammal(Animal):

    def go(self):
        print("I am a", self.name, "and I am GOING ")

class Rodent(Mammal):

    def gnaw(self):
        print("I am a", self.name, "and I am GNAWING")


class Bird (Animal):

    def fly(self):
        print("I am a", self.name, "and I am FLYING")

class LandBird(Bird):

    def swim(self):
        pass

class WaterBird(Bird):

    def swim(self):
        print("I am a", self.name, "and I am SWIMMING")

class Fish(Animal):

    def swim(self):
        print("I am a", self.name, "and I am SWIMMING")

