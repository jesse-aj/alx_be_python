monthly_income = int(input("Enter your monthly income "))
total_montly_expense = int(input("Enter your total monthly Expense "))

monthly_savings =  monthly_income - total_montly_expense
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"\n Your monthly savings are ${monthly_savings}")
print(f"\n Projected savings after one year, with interest, is : ${projected_savings} ")