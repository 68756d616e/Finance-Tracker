# Finance tracker

# What it should be able to do:
# Input employment salary and other income streams
# breakdown salary and tax brackets
# break down spending into groups
# 

# Welcome message
print("Welcome to your finance tracker")

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
year = month* 12

print(f"Your expenditures for each month is {month}")
question4 = input("Would you like to know your yearly expenditures? y/n ")
if question4 == 'y':
    print(f"Your expenditure is {year} each year!") # Provide a breakdown of each expenditure each year
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
