print("Welcome to the tip calculator.")
bill = int(input("What was the total bill?"))
percent = int(input("What percentage tip would you like the give?"))
num_people = int(input("How many people to split the bill?"))

percent = (percent/100) + 1

final = (bill*percent)/num_people
final = round(final, 2)

print(f"Each person should pay: ${final}")