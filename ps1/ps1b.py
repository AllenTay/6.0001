annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
r = 0.04

monthly_salary = annual_salary / 12 
money_needed = portion_down_payment * total_cost

months = 1
current_savings = 0

# you start with current savings of 0
# each month, you get monthly savings added to your savings 
while (money_needed - current_savings) > 100:
    if months % 6 == 0 and months != 0:
        monthly_salary += semi_annual_raise * monthly_salary
        annual_salary += semi_annual_raise * annual_salary
    monthly_saved = portion_saved * monthly_salary
    monthly_salary = annual_salary / 12 
    current_savings += monthly_saved
    current_savings += (current_savings * r) / 12
    months += 1

print('Number of months: ', months)