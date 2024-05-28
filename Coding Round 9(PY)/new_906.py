# 2 Private   ----> Can only be accessed within its class and not outside the class

class BankAccount:
   
   def __init__(self, account_number, balance):
      
      self.__account_number = account_number
      self.__balance = balance
    
   def __display_balance(self):
      
      print("Balance: ", self.__balance)
      print("Account Number: ", self.__account_number)

e1 = BankAccount(23456789, 54000)

# print(e1.__account_number)  # Here we are unable to access these both variables 
# print(e1.__balance)

# e1.__display_balance()       # Here we are unable to access the method too as everything has become private over here 

# By Placing a double underscore infront of a variable or a method name we are 
# declaring it as a private variable. This variable cannot be accessed normally 
# and requires a special method to access 

print(e1._BankAccount__account_number)
print(e1._BankAccount__balance)


e1._BankAccount__display_balance()

# By using the above method we accessed the variables as well as method too
# This is called as Name Mangling 



