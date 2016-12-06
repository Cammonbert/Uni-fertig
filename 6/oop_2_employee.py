######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# Objektorientiertes Programmieren I #
######################################
'''
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...) (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 points)

c) Draw a UML class diagram for your Employee class. (1 point)
		(Submit as PDF!)
		Hint: There is an editor called 'dia' which makes it easy
	  to create UML diagrams. It is available for Linux, MacOS
		and Windows (http://dia-installer.de/download/index.html).

'''

class Employee:
    def __init__(self, num, person, gender):
        self.number = num
        self.name = person
        self.gender = gender

        self.working = False
        self.balance = 0
        self.earn = 0

    def change_gender(self, gender):
        if self.gender == gender:
            print("Already " + gender)
        else:
            self.gender = gender
            return self.gender

    def change_name(self, name):
        self.name = name
        return self.name

    def work(self):
        if self.working is False:
            self.working = True
        else:
            self.working = False
        return self.working

    def sell_stuff(self, amount):
        self.balance += amount
        return self.balance

    def make_mistake(self, amount):
        self.balance -= 12*amount
        return self.balance

    def get_paid(self):
        self.balance -= 350
        self.earn += 350
        return self.balance

    def __str__(self):
        res = "*** Employee ***\n"
        res += "Employee ID:" + str(self.number) + "\n"
        res += "Name:" + self.name + "\n"
        res += "Gender: " + self.gender + "\n"
        res += "Currently working: " + str(self.working) + "\n"
        res += "Made " + str(self.balance) + " money until now." + "\n"
        res += "Got paid " + str(self.earn) + " money" + "\n"
        return res

if __name__ == "__main__":
    print("Employee application")

    olafemplo = Employee(1, "Olaf", "Male")
    olafemplo.work()
    olafemplo.sell_stuff(15)
    olafemplo.work()

    guentheremplo = Employee(2, "Guenther", "Female")
    guentheremplo.work()
    guentheremplo.change_name("Annika")
    guentheremplo.make_mistake(5)
    guentheremplo.sell_stuff(20)
    guentheremplo.work()

    earnieemplo = Employee(3, "Earnie", "Helikopter")
    earnieemplo.change_gender("Emu")
    earnieemplo.work()
    earnieemplo.make_mistake(300)
    earnieemplo.get_paid()
    earnieemplo.work()

    print(olafemplo)
    print(guentheremplo)
    print(earnieemplo)