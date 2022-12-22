GrossIncome = int(input("Enter your Gross Income"))
Dependents = int(input("Enter the number of Dependents-"))

Tax_1 = GrossIncome-10000-(Dependents*3000)
Final_Tax = Tax_1*0.2

print("Your tax is $",Final_Tax)
