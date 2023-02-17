def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def calculate_monthly_payment(loan_amount, interest_rate):
    monthly_interest_rate = interest_rate / 12
    monthly_payment = loan_amount * monthly_interest_rate
    return monthly_payment

def calculate_treadmill_calories():
    for minutes in [10, 15, 20, 25, 30]:
        calories_burned = minutes * 4.2
        print(f"After {minutes} minutes, you burned {calories_burned} calories.")
