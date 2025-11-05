# Variable declaration and assignment
monthly_income = input("Enter your monthly income: ")
tatal_montly_expenses = input("Enter your total monthly expenses: ")

# Calculate monthly savings
monthly_savings = int(monthly_income) - int(tatal_montly_expenses)

# Project annual savings 
annual_interest_rate = 0.05
projected_annual_saving = monthly_savings * 12 + (monthly_savings *12 * annual_interest_rate)

# Display monthly saings 
print("Your monthly savings are: $", monthly_savings)

# Display projected annual savings 
print("Projected saving after one year, with interest, is: $", projected_annual_saving)