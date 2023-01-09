# Finance tracker

# What it should be able to do:
# Input employment salary and other income streams
# breakdown salary and tax brackets
# break down spending into groups

# Welcome message
print("Welcome to your finance tracker")

# Tax breakdown - Include more options
print("Welcome to your yearly tax breakdown")
tax_question = input("""List of options you have:?
- breakdown - Tax breakdown
- hiw - how it works
- bracket = What is my tax bracket
- type - Type of taxes
please type here : """)

if tax_question == 'breakdown':
    tax_choice = input("Would you like an example or to calculate your own tax? type example or own")
    if tax_choice == 'example':
        name = input("What is your name? :")
        print(f"""If {name} earns £20,000 per year, paid monthly (so £1,667 per month).
Salary £20,000 - Yearly Income
Personal Allowance (£12,570) - This will not be taxed
Total £7,430 - Remaining when you subtract personal allowance from yearly salary
@20% £1,486 - The yearly amount taxed from the total remaining (£7430)
monthly tax - @20 yearly / 12 months = 123.83
PAYE deducted £1,485.60""")
        print() # Blank space
    elif tax_choice == 'own':
        user_salary = float(input("What is your yearly salary? :"))
        tax_year = user_salary # the equation
        salary_remaining = user_salary - 12570 # We subtract the personal income which will not be taxed
        to_tax = salary_remaining / 12 # We divide it by the amount of months
        month_tax =  0.2 * to_tax # We calculate the tax percentage - In this example it is %20 - change to fit whatever tax bracket the user is within
        year_tax = month_tax * 12
        print(f"""With a salary of {user_salary}, 12570 will be tax free, the remaining {salary_remaining} will be taxed. Your PAYE will be 20% of {salary_remaining}, which is {month_tax}
Each year you will pay {year_tax} tax""")
elif tax_question == 'hiw':
    how_it_works = '''Your income tax will be calculated based on the income tax band you're in. 
The more income you earn, the higher your tax band, which means you'll pay a higher amount of income tax. 
Income tax bands are designed to make paying tax as fair as possible to everyone, so that those who earn the most, 
contribute more.''' # How it works
    print(how_it_works) # Maybe remove the how it works and simple print
elif tax_question == 'bracket':
    user_salary2 = float(input("What is your salary? :")) # change
    if user_salary2 <= 12500: # change
        print(f"A salary of {user_salary2} is taxed %0") # change to correct rate
    elif user_salary2 > 12501 or user_salary2 >= 30000: # change to correct rate
        print(f"A salary of {user_salary2} is taxed %20") # change to correct rate
    elif user_salary2 >= 30001 or user_salary2 >= 45000: # change to correct rate
        print(f"A salary of {user_salary2} is taxed %30") # change to correct rate
    elif user_salary2 >40001 or user_salary2 >= 100000: # change to correct rate
        print(f"A salary of {user_salary2} is taxed %40") # change to correct rate
elif tax_question == 'type':
    print("You have two types of tax, Income tax and personal tax")
    print("Income tax: Income Tax is a tax you pay on your income. You do not have to pay tax on all types of income.")
    print("""Personal tax: The individual income tax (or personal income tax) is a tax levied on the wages, 
salaries, dividends, interest, and other income a person earns throughout the year. 
The tax is generally imposed by the state in which the income is earned.
""")
else:
    print("Please type breakdown for a yearly breakdown or hiw for how it works (lowercase)")

print() # empty space
# How much you spend a month on expenditures and the yearly amount
print("Please input 0 or the amount you spend for each expenditure")

rent_mortgage = float(input("How much do you spend each month on your rent or mortgage? £"))
groceries = float(input("How much do you spend each month on your groceries or house supply? £"))
transportation = float(input("How much do you spend on transportation each month? £"))
utility = float(input("How much do you spend each on on utilities, such as gas and electricity? £"))
entertainment = float(input("How much do you spend on entertainment or leisure each month> £"))
clothing = float(input("How much do you spend each month clothing or personal care items? £"))
health = float(input("How much do you spend each month on health care items? £"))
education = float(input("How much do you spend on education or training expenses? £"))
savings = float(input("How much do you save each month? £"))

month = rent_mortgage + groceries + transportation + utility + entertainment + clothing + health + education + savings
year = month * 12

# Each expenditure yearly
yearly_rent = rent_mortgage * 12
yearly_groceries = groceries * 12
yearly_transportation = transportation * 12
yearly_utility = utility * 12
yearly_entertainment = entertainment * 12
yearly_clothing = clothing * 12
yearly_health = health * 12
yearly_education = education * 12
yearly_savings = savings * 12

print(f"Your expenditures for each month is {month}")
question4 = input("Would you like to know your yearly expenditures? y/n ")
if question4 == 'y':
    print(f"Your expenditure is {year} each year!") # Provide a breakdown of each expenditure each year

    # A breakdown of each expenditure multiplied by the amount of months within a year
    question5 = input("Would you like to have a breakdown of your yearly expenditures (y/n) ")
    if question5 == 'y':
        print(f"""
    Each year you spend £{yearly_rent} on rent, £{yearly_groceries} on groceries, £{yearly_transportation} on transportation, £{yearly_utility} on utilities,
    £{yearly_entertainment} on entertainment, £{yearly_clothing} on clothing, £{yearly_health} on your health, £{yearly_education} on your education, £{yearly_savings} on your savings.
        """)
    elif question5 == 'n':
        print("No works for breakdown")
else:
    print("Please type y for yes or n for no")

# inital question, providing the options the user can choose

# Outcome - The amount the user spends either Weekly, monthly or yearly - Provide variables below - This is just test questions
question1 = input("Would you like to know you weekly, monthly or yearly outcomes? y or n :")
if question1 == 'y':
    daily_travel = float(input("How much do you spend on travel daily? £"))
    daily_food = float(input("How much do you spend on food daily? £"))

    question = input("Would you like to know your Weekly, Monthly, Yearly or entire outcome?")

    if question == 'weekly':
        total_daily = daily_travel + daily_food * 5 # There will be a future question asking the amount of days
        print(f"You spend {total_daily} in a week on travel and food")
    elif question == 'monthly':
        total_monthly = (daily_travel + daily_food) * 5 * 4
        print(f"you spend {total_monthly} a month on food and travel!")
    elif question == 'yearly':
        total_yearly = (daily_travel + daily_food) * 5 * 4 * 12
        print(total_yearly)
    elif question == 'entire':
        entire1 = daily_travel * 250 # This is a year of travel without holidays
        entire2 = daily_food * 250 # This is a year of food without holidays
        print(f"You spend {entire1} on travel and {entire2} on food within 1 year") # This will display both travel and food expense amount for the year
    else:
        print("Please type in lower case weekly, monthly, yearly or no to move on")
elif question1 == 'no':
    print("Ok")
else:
    print("In lowercase y for yes or n for no")

# Breakdown of Yearly salary
salary = float(input("What is your yearly salary? £"))

months = salary / 12
weekly = salary / 12 / 4
daily = salary / 250

print(f"With a salary of £{salary}, you will earn {months} a month, {weekly} a week and {daily} a day, before tax.")

# Daily outcome of the user
print("Please answer the following questions either with 0 or your relative outcome amount")

# List of questions to conclude a daily outcome
travel = float(input("How much do you spend on travel everyday? Answer: £"))
food = float(input("How much do you spend on food everyday? Answer: £"))
# The user will be able to add additonal daily costs
total = travel + food
print(f"Your daily outcome is £{total}")
