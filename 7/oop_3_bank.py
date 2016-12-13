######################################
# Symbolische Programmiersprache     #
# WS 2016/2017                       #
# Objektorientiertes Programmieren I #
######################################

# !!!REQUIREMENT!!!
# Submit this .py file containing your code and one
# PDF file containing the UML diagrams!!

'''
Exercise: 7 points

a) Fill out the missing parts in the code below (5 points)
b) Draw a UML diagram for the application. (2 points)

HINTS:
* You will have to replace the 'pass' statements with some
  meaningful code. Pay attention to the comments which
  describe what is expected.
* You may want to comment out parts of the main application
  while coding! If you just run this, you will get errors at first!


'''

#######################################
# CLASSES FOR THE BANKING APPLICATION #
#######################################

class Customer:
    ''' objects of this class represent customers.
    The customer ID is supposed to be assigned automatically
    when a new customer object is created.
    Attributes:
    - first name
    - last name
    - age
    '''
    cust_id = 0
    # CONSTRUCTOR
    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age
        Customer.cust_id += 1
        self.ID = self.cust_id


    # INSTANCE METHODS
    def increment_age(self):
        '''Age + 1'''
        self.age += 1
        return self.age

    def __str__(self):
        return "*** Customer Info ***" \
               + "First Name:" + str(self.first_name) \
               + " Last Name:" + str(self.last_name) \
               + "Age: " + str(self.age)

    # SETTERS
    def set_lastname(self, ln):
        ''' sets the last name of a customer '''
        self.last_name = ln
        return self.last_name

    # STATIC METHODS
    ''' write a method called print_info here that prints
    out how many customers have been created so far '''
    def print_info(self):
            print("Anzahl Customers: " + Customer.custcounter)

class Account:
    ''' Objects created from this class
    represent accounts.
    Account ID is assigned automatically when creating
    an account object.
    Attributes:
    - number
    - holder (object of class 'Customer')
    - balance '''

    
    # CONSTRUCTOR
    id = 0
    def __init__(self, holder):
        ''' the initialization method is called right after
        an object has been created. used to initialize attributes'''
        self.holder = holder
        self.balance = 0
        self.id += 1
        self.acc_id = self.id


    # INSTANCE METHODS
    def withdraw(self, amount):
        ''' withdraw an amount of money from an account object:
        subtract the amoun from the balance, does not allow a
        negative balance. Returns the amount that was actually
        withdrawn from the account. '''
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount
        return amount
        
    def deposit(self, amount):
        ''' deposit an amount of money into an account:
        add the amount of money to the balance '''
        self.balance += amount

    def set_holder(self, new_holder):
        ''' change the account holder.
        We could perform validation here. '''
        self.holder = new_holder
        
    def __str__(self):
        ''' returns a string describing the account object '''
        return "[Account: ID=" + str(self.acc_id) \
              + " BALANCE=$" + str(self.balance) \
              + " HOLDER=" + str(self.holder)+ "]"


class Bank:
    ''' class for objects that represent a bank
    Attributes:
    - name
    - accounts (dictionary, listed by account ID)
    - customers (dictionary, listed by customer ID) '''
    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        self.accounts = dict()
        self.customers = dict()
        # list accounts by account ID
        # list customers by ID

    # INSTANCE METHODS
    def print_accounts(self):
        ''' print out all accounts of the bank '''
        print("\n** ACCOUNTS **")
        '''
        Hier komm ich nicht weiter
        '''

    def print_customers(self):
        ''' prints out all the customers of the bank '''
        print("\n** CUSTOMERS **")
        '''
        Hier komm ich nicht weiter
        '''

    def add_customer(self, customer):
        ''' adds a customer object to the bank's customers '''
        self.customers[customer.ID] = customer

    def add_account(self, account):
        ''' adds an account object to the bank's accounts '''
        self.accounts[account.acc_id] = account

    def deposit(self, acc_id, amount):
        ''' deposit money into the account '''
        if acc_id == Account.id:
            Account.deposit(self,amount)

    def withdraw(self, cust_id, acc_id, amount):
        ''' withdraw money from the account with the given ID,
        but only if its holder has the given customer ID.
        Returns the amount of money (=cash)'''
        if acc_id == Account.id:
            if cust_id == Customer.ID:
                Account.withdraw(self, amount)
                return amount

    def __str__(self):
        ''' returns a descriptive string for the bank '''
        return "[Bank: " + self.name \
               + " Customers=$" + str(self.customers) \
               + " Accounts=" + str(self.accounts) + "]"



##############################
# BANKING APPLICATION - MAIN #
##############################

if __name__ == "__main__":
    # Create a new bank object
    bank = Bank("PYTHON-BANK")
    print(bank)

    # Create a few customers and add them to the bank object
    anne = Customer("Anne", "Friedrich", 85)
    bank.add_customer(anne)
    stefan = Customer("Stefan", "Thater", 76)
    bank.add_customer(stefan)
    maja = Customer("Maja", "Biene", 2)
    bank.add_customer(maja)

    # Print out all the customers of the bank
    bank.print_customers()
    
    # Create a few accounts and add them to the bank object
    annesAcc1 = Account(anne)
    bank.add_account(annesAcc1)
    annesAcc2 = Account(anne)
    bank.add_account(annesAcc2)
    stefansAcc = Account(stefan)
    bank.add_account(stefansAcc)
    majasAcc = Account(maja)
    bank.add_account(majasAcc)

    # Print out all the accounts of the bank
    bank.print_accounts()

    # Deposit money into accounts
    print("\nAnne deposits $300 into account with ID 1.")
    bank.deposit(1, 400)
    print("Stefan's customer ID:", stefan.cust_id)
    print("Stefan deposits $1000 into account with ID 2.")
    bank.deposit(2, 1000)

    # Print out all the accounts of the bank
    bank.print_accounts()

    # Withdraw money from some accounts
    print("\nAnne tries to withdraw from Stefan's account.")
    cash = bank.withdraw(0, 2, 100)
    print("Anne got:", cash)
    print("Now Anne tries to withdraw from her own account.")
    cash = bank.withdraw(0,1,100)
    print("Anne got:", cash)

    # Number of customers
    '''print("")
    Customer.print_info()'''
    print("Number of customers that have been added to the bank:", len(bank.customers.keys()))   
    
