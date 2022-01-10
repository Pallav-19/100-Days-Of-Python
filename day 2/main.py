print("Welcome to the tip calculator!")
totalBill = float(input("What Was the Total Bill? "))
tipPercent = int(input("How much tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))
bill = totalBill // persons
finalSplit = round(bill * (tipPercent / 100),2)
print("Each person should pay: $" + str(finalSplit))

