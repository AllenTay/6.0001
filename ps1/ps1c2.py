starting_salary = int(input("Enter the starting salary: "))
semi_annual_raise = 0.07
annual_return = 0.04
total_cost = 1000000
down_payment = total_cost * 0.25
months = 36

min_rate = 0        #0%
max_rate = 10000    #100%

portion_saved = int((max_rate + min_rate) / 2)
steps = 0
found = False

while abs(min_rate - max_rate) > 1:
    steps +=1
    annual_salary = starting_salary
    monthly_saved = (annual_salary/12.0) * (portion_saved/10000)
    current_savings = 0.0

    for month in range(1, months+1):
        monthly_return = current_savings * (annual_return/12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - down_payment) < 100 :
            min_rate = max_rate
            found = True
            break

        elif current_savings > down_payment + 100:
            break

        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_saved = (annual_salary/12.0) * (portion_saved/10000)

    if current_savings < down_payment - 100:
        min_rate = portion_saved
    elif current_savings > down_payment + 100 :
        max_rate = portion_saved

    portion_saved = (max_rate+min_rate)//2

if found:
    print("Steps in bisection search: " +  str(steps))
    print("Best savings rate :        " + str(portion_saved/10000))
else:
    print("It is not possible to make down payment in three years")