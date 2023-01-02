# Finance tracker

# What it should be able to do:
# Input employment salary and other income streams
# breakdown salary and tax brackets
# break down spending into groups
# 

# Welcome message
print("Welcome to your finance tracker")

# inital question, providing the options the user can choose

# Outcome - The amount the user spends either daily, weekly or monthly - Provide variables below

# Daily outcome of the user
print("Please answer the following questions either with 0 or your relative outcome amount")

# List of questions to conclude a daily outcome
travel = float(input("How much do you spend on travel everyday? Answer: £"))
food = float(input("How much do you spend on food everyday? Answer: £"))
other = input("Do you have any other daily outcomes? y/n Answer: ")
if other == 'y':
    print("Yes")
elif other == 'n':
    print("No")
else:
    print("Please type y or no") 
total = travel + food
print(f"Your daily outcome is £{total}")