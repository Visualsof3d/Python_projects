"""
This is the simple countdown project which display the remaining days left to achieve your goal.
"""
import datetime

print("Enter your goal with a deadline and separate it by colon(:)")
input_param = input("example - learn python(goal):30.11.2023(deadline)\n")
user_input = input_param.split(":")

goal = user_input[0]
deadline = user_input[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

# Calculating how many days left from now till deadline
# Learn DevOps:15.01.2024
time_left = deadline_date - today_date
print(f"\nDear user, you have {time_left.days} days left to complete your goal of {goal}.")
