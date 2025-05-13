# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Anonymous"
    
    @classmethod
    def change_bank_name(cls, bank_name):
        cls.bank_name = bank_name
        print(f"bank name Changed to {cls.bank_name}")

    @classmethod
    def show_name(cls):
        print(f"bank name is {cls.bank_name}")

bank1 = Bank()
bank1.show_name()
bank2 = Bank()
bank2.change_bank_name("Meezan Bank")
bank3 = Bank()
bank3.show_name()