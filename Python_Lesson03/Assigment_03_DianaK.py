# create user input variables 
money_start = input("Enter the amount of your current savings: ")
saving_years = input("Enter the numbers of years to save for: ")
interest_rate = input("Enter the savings interest rate (to 1 d.p): ")

# convert input into integer or float and check type 
print(type(int(money_start)))
print(type(int(saving_years)))
print(type(float(interest_rate)))

# calculate savings amount
money_result = int(money_start) *float(interest_rate) *int(saving_years)

# print expected output
print(f"Your savings after {int(saving_years)} years: ${int(money_result)}")
savings_goal = int(money_result) >10000
print(f"Will you have more than $10,000 in savings? {savings_goal}")