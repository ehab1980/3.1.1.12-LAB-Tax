income = float(input("Enter the annual income: "))
# Put your code here.
if income <= 85528:
    tax = (income * 0.18) - 556.02
    if (income * 0.18) - 556.02< 0:
        tax =0
else:
    tax = 14839 + (0.32 * (income - 85528))
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
