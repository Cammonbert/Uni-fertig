######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# Objektorientiertes Programmieren I #
######################################


'''
Exercise 1: (5 points)

a) Using the slides & the script, put together a file
    containing the complete Account class.
    Each method must have a documentation string at the
    beginning which describes what the method is doing.
    (1 points)

b) Create a main application where you create a number of accounts.
    Play around with depositing / withdrawing money.
    Change the account holder of an account using a setter method.
    (1 point)

c) Change the withdraw function such that the minimum balance
    allowed is -1000.
    (1 point)

d) Write a function apply_interest(self) which applies an interest
    rate of 1.5% to the current balance and call it on your objects.
    (1 points)

e) Draw a UML diagram representing your Account class. (1 point)

'''

class Account:
    '''Erstellen der Attribute für Account'''
    def __init__(self, num, person):
        self.balance = 0
        self.number = num
        self.holder = person

    '''Geldbetrag abheben, falls Kontostand ausreichend'''
    def withdraw(self, amount):
        if amount <= 0:
            print("Negativen Betrag abheben? Benutz lieber deposit()")
        else:
            if self.balance-amount>=-1000:  #Wenn nicht unter 0 gegangen werden darf 0 anstatt -1000 benutzen
                self.balance -= amount
                return self.balance
            else:
                print("Zu wenig Guthaben. \nDerzeitiges Guthaben beträgt: ",self.balance)

    '''Geldbetrag einzahlen'''
    def deposit(self, amount):
        if amount<=0:
            print("Negativen Wert einzahlen? Benutz lieber withdraw()")
        else:
            self.balance += amount
            return self.balance

    '''Setzt Person, der das Konto gehört'''
    def setholder(self, person):
        self.holder = person

    '''String abruf eines Accounts'''
    def __str__(self):
        res = "*** Account Info ***\n"
        res += "Account ID:" + str(self.number) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res

    '''Erhöht/Senkt Kontostand bei Abruf um 1.5%'''
    def apply_interest(self):
        self.balance += (self.balance*0.015)
        if self.balance <= -1000:
            print("Kontosperrung, bitte Schulden beheben")
            return self.balance
        else:
            return self.balance

'''Main Methode zum benutzen von Methoden'''
if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    '''Erstellt Peters Account, gibt ihm 5000 aufs Konto und frägt Accountdetails ab'''
    petersacc = Account(1, "Peter")
    petersacc.deposit(5000)
    print(petersacc)
    '''Erstellt Annas Account, gibt ihr 1000 aufs Konto und testet einen Fehler beim einzahlen
       Danach gibt es die Accountdetails aus'''
    annasacc = Account(2, "Anna")
    annasacc.deposit(1000)
    annasacc.deposit(-100)
    print(annasacc)
    '''Erstellt Udos Account, zieht 300 ab, gibt ihm 2000 und zieht ihm dann 1234 ab
       Danach gibt es die Accountdetails aus'''
    udosacc = Account(3, "Udo")
    udosacc.withdraw(300)
    udosacc.deposit(2000)
    udosacc.withdraw(1234)
    print(udosacc)
    '''Erstellt Julias Account, verändert den Inhaber von Julia zu Kuh und zieht 1000 vom Kontostand ab
       Danach gibt es die Kontodetails aus
       Dann wird der Kontostand um 1.5% erhöht --> hier negativ weil Kontostand unter 0
       Danach wieder Ausgabe des Kontostands'''
    juliasacc = Account(4, "Julia")
    juliasacc.setholder("Kuh")
    juliasacc.withdraw(1000)
    print(juliasacc)
    juliasacc.apply_interest()
    print(juliasacc)
