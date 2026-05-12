print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_value = bill * tip / 100
full_bill = bill + tip_value

person_value = full_bill / people

print(f"Each person should pay ${person_value:.2f}")