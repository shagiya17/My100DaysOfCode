print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
each_person = bill_with_tip / people
final_amount = round(each_person, 2)
print(f"Each person should pay: ${final_amount}")
