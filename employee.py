"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, wage, hours, commissionType, commissionValue, numberOfContracts):
        self.name = name
        self.contractType = contractType
        self.wage = wage
        self.hours = hours
        self.commissionType = commissionType
        self.commissionValue = commissionValue
        self.numberOfContracts = numberOfContracts

    def get_pay(self):
        if self.contractType == 'salary':
            pay = self.wage
        else:
            pay = self.wage * self.hours

        if self.commissionType == 'fixed':
            pay += self.commissionValue
        elif self.commissionType == 'contracts':
            pay += ((self.commissionValue) * (self.numberOfContracts))

        return pay

    def __str__(self):
        string = self.name + ' works on a '
        if (self.contractType == 'salary'):
            string += 'monthly salary of ' + str(self.wage)
        else:
            string += 'contract of ' + str(self.hours) + ' hours at ' + str(self.wage) + '/hour'
        print (string)
        if self.commissionType == 'contracts':
            string += ' and receives a commission for ' + str(self.numberOfContracts) + ' contract(s) at ' + str(self.commissionValue) + '/contract.'
        elif self.commissionType == 'fixed':
            string += ' and receives a bonus commission of ' + str(self.commissionValue) + '.'
        else:
            string += '.'
        string += ' Their total pay is ' + str(self.get_pay()) + '.'
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', 4000, 0, "none", 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'contract', 25, 100, "none", 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', 3000, 0, "contracts", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'contract', 25, 150, "contracts", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'salary', 2000, 0, "fixed", 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'contract', 30, 120, "fixed", 600, 0)
