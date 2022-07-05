annual_salary = float(input('Enter your annual salary: '))
salary = annual_salary
numGuesses = 0
high = 1
low = 0
ans = (high + low) / 2.0 

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
        months += 1
    return months


counter = trial(1, salary) # Check if using 100 percent will work 
 
if counter > 36:
    print('It is not possible to pay the down payment in 3 years')

else:
    bean = trial(ans, salary)
    found = False
    
    while found == False:
        numGuesses += 1
        if bean >= 36: 
            low = ans # Ans is currently 0.5 and we will set low = 0.5 
            ans = (high + low) / 2.0 # Ans = 0.75 
            print('Ans = ', str(ans))
        
        if bean <= 36:  
            high = ans
            ans = (high + low) / 2.0
            print('Ans = ', str(ans))
        
        bean = trial(ans, salary) # bean is 26

        if abs(low - high) <= 0.01:
            found = True

    print('Best savings rate: ', ans)
    print('Steps in bisection search ', numGuesses)
        
        


    