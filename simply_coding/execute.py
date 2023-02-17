import formulas

# Fahrenheit to Celsius
fahrenheit = 80
celsius = formulas.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")

# Monthly payment calculation
loan_amount = 10000
interest_rate = 5
monthly_payment = formulas.calculate_monthly_payment(loan_amount, interest_rate)
print(f"For a loan amount of {loan_amount} and an interest rate of {interest_rate}%, the monthly payment is ${monthly_payment:.2f}.")

# Treadmill calories burned
formulas.calculate_treadmill_calories()
