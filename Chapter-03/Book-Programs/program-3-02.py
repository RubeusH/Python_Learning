OVERTIME_LIMIT = 40.0
OVERTIME_RATE = 1.5
REGULAR_HOURS = 40
OVERTIME_MULTIPLIER = 1.5
hours_worked = float(input("How many hours did you work? "))
hourly_rate = float(input("What is your hourly rate? "))
wage = 0.0
if hours_worked > OVERTIME_LIMIT:
    wage = REGULAR_HOURS * hourly_rate + OVERTIME_MULTIPLIER * (hours_worked - REGULAR_HOURS)
    print("Your wage is: $" + format(wage, '.2f'))
else:
    wage = hours_worked * hourly_rate
    print("Your wage is: $" + format(wage, '.2f'))
