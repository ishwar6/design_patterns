# naive implementation of the ATM cash dispensing mechanism without using CoR. 
# The naive approach have a single method with conditional logic to handle the entire cash dispensing process.

class ATMMachine:
    def withdraw(self, amount):
        if amount % 100 != 0:
            print("Amount must be in multiples of 100")
            return

        notes_2000 = notes_500 = notes_100 = 0

        if amount >= 2000:
            notes_2000, amount = divmod(amount, 2000)
        
        if amount >= 500:
            notes_500, amount = divmod(amount, 500)

        if amount >= 100:
            notes_100, amount = divmod(amount, 100)

        print(f"Dispensing {notes_2000} note(s) of Rs 2000")
        print(f"Dispensing {notes_500} note(s) of Rs 500")
        print(f"Dispensing {notes_100} note(s) of Rs 100")

# Client Code
atm = ATMMachine()
atm.withdraw(3600)


#output
# Dispensing 1 note(s) of Rs 2000
# Dispensing 3 note(s) of Rs 500
# Dispensing 1 note(s) of Rs 100
