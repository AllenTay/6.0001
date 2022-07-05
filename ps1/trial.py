from turtle import down


annual_salary = float(input('Enter your annual salary: '))
salary = annual_salary

def trial(portion, salary):
    semi_annual_raise = 0.07
    r = 0.04
    total_cost = 1000000
    down_payment = 0.25 * total_cost
    months = 1
    current_savings = 0
    monthly_salary = salary / 12 

    while (down_payment - current_savings) > 100:
        if months % 6 == 0 and months != 0:
            monthly_salary += semi_annual_raise * monthly_salary
            salary += semi_annual_raise * salary
        monthly_salary = salary / 12
        monthly_saved = portion * monthly_salary
        current_savings += monthly_saved
        current_savings += (current_savings * r) / 12
        print(str(current_savings))
        months += 1
    return months

a  = 0.4411
b  = 0.2206
bean = trial(a, salary)
print(str(bean))