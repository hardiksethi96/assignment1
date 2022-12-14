print("Enter your details: ")
gross_income = int(input("Enter your gross income (in dollars): "))
num_of_dependents = int(input("Enter number of dependents: "))
taxable_income = gross_income - 10000 - (3000 * num_of_dependents)
tax = taxable_income * (20/100)
if (tax>0):
    print("Your applicable tax is " + str(tax) + "$")
else:
    print("You have to pay no tax")
